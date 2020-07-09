# -*- coding: utf-8 -*-
"""
pyud.client
Copyright (c) 2020 William Lee

This file is part of pyud.

pyud is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

pyud is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with pyud.  If not, see <https://www.gnu.org/licenses/>.
"""

import json
from typing import AsyncGenerator, Generator, List, Optional, Union
from urllib import request
from urllib.parse import quote as url_quote

import aiohttp

from . import definition

BASE_URL = "https://api.urbandictionary.com/v0/"
DEFINE_BY_TERM_URL = BASE_URL + "define?term={}&page={}"
DEFINE_BY_ID_URL = BASE_URL + "define?defid={}"
RANDOM_URL = BASE_URL + "random"


class ClientBase:
    """
    Base class for the Client and AsyncClient
    """

    def _parse_definitions_from_json(
        self, data: Union[str, bytes, bytearray]
    ) -> Optional[List['definition.Definition']]:
        """
        Returns a list of Definitions from JSON

        The format of the JSON is a single array of definition objects
        under the key 'list' in the JSON document
        """

        try:
            parsed_data = json.loads(data, strict=False)
        except json.JSONDecodeError:
            raise Exception(
                "JSON was not given in the correct format"
            ) from None

        if 'list' not in parsed_data or not parsed_data['list']:
            return

        definitions_list = parsed_data['list']
        definitions = []

        for dictionary in definitions_list:
            try:
                definitions += [definition.Definition(self, **dictionary)]
            except TypeError:
                pass

        return definitions if definitions else None

    def __str__(self):
        return "Instance of {0.__name__}".format(type(self))

    def __repr__(self):
        return "{0.__name__}()".format(type(self))


class Client(ClientBase):
    """
    Synchronous client for the Urban Dictionary API
    """

    def _fetch_definitions(
        self, url: str
    ) -> Optional[List['definition.Definition']]:
        """
        Fetch definitions from the API url given
        """
        with request.urlopen(url) as response:  # nosec
            return self._parse_definitions_from_json(
                response.read().decode('utf-8')
            )

    def define(
        self, term: str, *, page: int = 1
    ) -> Optional[List['definition.Definition']]:
        """Finds definitions for a given term from a given page,
        up to a maximum of 10 definitions.

        :param term: The term to find definitions for
        :type term: str
        :param page: The page of the definitions to return, defaults to 1
        :type page: int
        :return: A list of definitions or :data:`None` if not found
        :rtype: Optional[List[Definition]]
        """
        return self._fetch_definitions(
            DEFINE_BY_TERM_URL.format(url_quote(term), page)
        )

    def define_iter(
        self, term: str, limit: Optional[int] = None
    ) -> Generator['definition.Definition', None, None]:
        """Finds definitions for a given term up to a certain number of definitions,
        returning a generator.

        :param term: The term to find definitions for
        :type term: str
        :param limit: The maximum number of definitions to return, defaults to :data:`None`
        :type limit: Optional[int]
        :return: A generator of the definitions
        :rtype: Generator[Definition, None, None]
        """
        count = 0
        page = 1
        yielding = True
        while yielding:
            definitions = self.define(term, page=page)
            if definitions is None:
                break
            for d in definitions:
                yield d
                count += 1
                if limit is not None and count >= limit:
                    yielding = False
                    break
            else:
                page += 1

    def from_id(self, defid: int) -> Optional['definition.Definition']:
        """Finds a definition by ID

        :param defid: The ID of the definition
        :type defid: int
        :return: The definition corresponding to the ID or :data:`None` if not found
        :rtype: Optional[Definition]
        """
        definitions = self._fetch_definitions(DEFINE_BY_ID_URL.format(defid))

        return definitions[0] if definitions else None

    def random(self, *, limit: int = 10) -> List['definition.Definition']:
        """Returns a random list of definitions

        :param limit: The number of definitions to return, defaults to 10
        :type limit: int
        :return: A list of definitions
        :rtype: List[Definition]
        """
        definitions = []
        for _ in range(limit // 10 + 1):
            definitions += self._fetch_definitions(RANDOM_URL)

        return definitions[:limit]


class AsyncClient(ClientBase):
    """
    Asynchronous client for the Urban Dictionary API
    """

    async def _fetch_definitions(
        self, url: str
    ) -> Optional[List['definition.Definition']]:
        """
        Fetch definitions from the API url given
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:  # nosec
                return self._parse_definitions_from_json(await response.text())

    async def define(
        self, term: str, *, page: int = 1
    ) -> Optional[List['definition.Definition']]:
        """Finds definitions for a given term from a given page asynchronously,
        up to a maximum of 10 definitions.

        :param term: The term to find definitions for
        :type term: str
        :param page: The page of the definitions to return, defaults to 1.
        :type page: int
        :return: A list of definitions or :data:`None` if not found
        :rtype: Optional[List[Definition]]
        """
        return await self._fetch_definitions(
            DEFINE_BY_TERM_URL.format(url_quote(term), page)
        )

    async def define_iter(
        self, term: str, limit: Optional[int] = None
    ) -> AsyncGenerator['definition.Definition', None]:
        """Finds definitions for a given term up to a certain number of definitions,
        returning a generator.

        :param term: The term to find definitions for
        :type term: str
        :param limit: The maximum number of definitions to return, defaults to :data:`None`
        :type limit: Optional[int]
        :return: An asynchronous generator of the definitions
        :rtype: AsyncGenerator[Definition, None]
        """
        count = 0
        page = 1
        yielding = True
        while yielding:
            definitions = await self.define(term, page=page)
            if definitions is None:
                break
            for d in definitions:
                yield d
                count += 1
                if limit is not None and count >= limit:
                    yielding = False
                    break
            else:
                page += 1

    async def from_id(self, defid: int) -> Optional['definition.Definition']:
        """Finds a definition by ID asynchronously

        :param defid: The ID of the definition
        :type defid: int
        :return: The definition corresponding to the ID or :data:`None` if not found
        :rtype: Optional[Definition]
        """
        definitions = await self._fetch_definitions(
            DEFINE_BY_ID_URL.format(defid)
        )

        return definitions[0] if definitions else None

    async def random(
        self, *, limit: int = 10
    ) -> List['definition.Definition']:
        """Returns a random list of definitions

        :param limit: The number of definitions to return, defaults to 10
        :type limit: int
        :return: A list of definitions
        :rtype: List[Definition]
        """
        definitions = []
        for _ in range(limit // 10 + 1):
            definitions += await self._fetch_definitions(RANDOM_URL)

        return definitions[:limit]

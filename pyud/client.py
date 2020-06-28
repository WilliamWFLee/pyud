# -*- coding: utf-8 -*-
"""
pyud.client
~~~~~~~~~~~

:copyright: 2020 William Lee
:license: GNU GPL v3.0, see LICENSE
"""

import json
from typing import List, Optional, Union
from urllib import request

from .definition import Definition
import aiohttp

BASE_URL = "https://api.urbandictionary.com/v0/"
DEFINE_BY_TERM_URL = BASE_URL + "define?term={}"
DEFINE_BY_ID_URL = BASE_URL + "define?defid={}"
RANDOM_URL = BASE_URL + "random"


class ClientBase:
    """
    Base class for the Client and AsyncClient
    """
    def _from_json(
        self, data: Union[str, bytes, bytearray]
    ) -> Optional[List[Definition]]:
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
                definitions += [Definition(**dictionary)]
            except TypeError:
                pass

        return definitions if definitions else None


class Client(ClientBase):
    """
    Synchronous client for the Urban Dictionary API
    """
    def _fetch_definitions(self, url: str) -> Optional[List[Definition]]:
        """
        Fetch definitions from the API url given
        """
        with request.urlopen(url) as response:
            return self._from_json(response.read().decode('utf-8'))

    def define(self, term: str) -> Optional[List[Definition]]:
        """
        Finds definitions for a given term
        """
        return self._fetch_definitions(DEFINE_BY_TERM_URL.format(term))

    def from_id(self, defid: int) -> Optional[Definition]:
        """
        Finds a definition by ID
        """
        definitions = self._fetch_definitions(DEFINE_BY_ID_URL.format(defid))

        return definitions[0] if definitions else None

    def random(self, *, limit: int = 10) -> List[Definition]:
        """
        Returns a random list of definitions
        """
        definitions = self._fetch_definitions(RANDOM_URL)

        return definitions[:limit]


class AsyncClient(ClientBase):
    """
    Asynchronous client for the Urban Dictionary API
    """
    async def _fetch_definitions(self, url: str) -> Optional[List[Definition]]:
        """
        Fetch definitions from the API url given
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return self._from_json(await response.text())

    async def define(self, term: str) -> Optional[List[Definition]]:
        """
        Finds definitions for a given term
        """
        return await self._fetch_definitions(DEFINE_BY_TERM_URL.format(term))

    async def from_id(self, defid: int) -> Optional[Definition]:
        """
        Finds a definition by ID
        """
        definitions = await self._fetch_definitions(
            DEFINE_BY_ID_URL.format(defid)
        )

        return definitions[0] if definitions else None

    async def random(self, *, limit: int = 10) -> List[Definition]:
        """
        Returns a random list of definitions
        """
        definitions = await self._fetch_definitions(RANDOM_URL)

        return definitions[:limit]

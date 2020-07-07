# -*- coding: utf-8 -*-
"""
pyud.reference
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

from typing import List, Optional, Union

from . import client, definition


class ReferenceBase:
    """
    Represents a reference in an Urban Dictionary definition.
    """

    def __init__(
        self, client: Union['client.Client', 'client.AsyncClient'], word: str
    ):
        self.client = client
        self.word = word


class Reference(ReferenceBase):
    """
    The class of references in :paramref:`Definition.references`
    when :class:`Client` is used to obtain those definitions

    Instances of this class should not obtained directly, and should instead be obtained
    by accessing the :paramref:`~Definition.references` attribute
    on an instance of :class:`Definition`.
    """
    def define(self) -> Optional[List['definition.Definition']]:
        """Returns definitions for the reference

        :return: A list of definitions, or :data:`None` if none are found
        :rtype: Optional[List[Definition]]
        """
        return self.client.define(self.word)


class AsyncReference(ReferenceBase):
    """
    The class of references in :paramref:`Definition.references`
    when :class:`AsyncClient` is used to obtain those definitions

    Instances of this class should not obtained directly, and should instead be obtained
    by accessing the :paramref:`~Definition.references` attribute
    on an instance of :class:`Definition`.
    """
    async def define(self) -> Optional[List['definition.Definition']]:
        """Returns definitions for the reference asynchronously

        :return: A list of definitions, or :data:`None` if none are found
        :rtype: Optional[List[Definition]]
        """
        return await self.client.define(self.word)

# -*- coding: utf-8 -*-
"""
pyud.generator
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

from typing import Optional

from . import definition


class AsyncDefinitionGenerator:
    """
    An asynchronous generator for definitions.
    For compatibility with Python 3.5.
    """

    def __init__(
        self, definition_getter, limit: Optional[int] = None,
    ):
        self.definition_getter = definition_getter
        self.limit = limit
        self._page = 1

    def __aiter__(self) -> 'AsyncDefinitionGenerator':
        self._counter = 0
        self._index = 0
        self._definitions = []

        return self

    async def __anext__(self) -> 'definition.Definition':
        if self.limit is not None and self._counter >= self.limit:
            raise StopAsyncIteration
        if self._index <= len(self._definitions):
            self._definitions = await self.definition_getter(page=self._page)
            self._page += 1
            self._index = 0
        if not self._definitions:
            raise StopAsyncIteration

        definition = self._definitions[self._index]

        self._counter += 1
        self._index += 1

        return definition

# -*- coding: utf-8 -*-
"""
pyud.definition
~~~~~~~~~~~~~~~

:copyright: 2020 William Lee
:license: GNU GPL v3.0, see LICENSE
"""

from datetime import datetime as dt
from typing import Any, Dict, Union


class Definition:
    """Represents an Urban Dictionary definition"""
    def __init__(
        self,
        *,
        defid: int,
        word: str,
        definition: str,
        author: str,
        thumbs_up: int,
        thumbs_down: int,
        example: str,
        permalink: str,
        written_on: str,
        **attrs: Dict[str, Any],
    ):
        """Instantiates an instance of an Urban Dictionary definition

        :param defid: The ID of the definition
        :type defid: int
        :param word: The word that is being defined
        :type word: str
        :param definition: The definition description
        :type definition: str
        :param author: The author of the description
        :type author: str
        :param thumbs_up: The number of thumbs-up given to the definition
        :type thumbs_up: int
        :param thumbs_down: The number of thumbs-down given to the definition
        :type thumbs_down: int
        :param example: An example usage of the definition
        :type example: str
        :param permalink: The permalink for the definition
        :type permalink: str
        :param written_on: The date and time the definition was written as RFC 3339
        :type written_on: str
        """
        self.defid = defid
        self.word = word
        self.definition = definition
        self.author = author
        self.thumbs_up = thumbs_up
        self.thumbs_down = thumbs_down
        self.example = example
        self.permalink = permalink

        # Parses the RFC 3339 timestring to a naive datetime object
        self.written_on = dt.strptime(written_on, "%Y-%m-%dT%H:%M:%S.%fZ")

        # Excess attributes are added
        for name, value in attrs.items():
            setattr(self, name, value)

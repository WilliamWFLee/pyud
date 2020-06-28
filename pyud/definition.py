# -*- coding: utf-8 -*-
"""
pyud.definition
~~~~~~~~~~~~~~~

:copyright: 2020 William Lee
:license: GNU GPL v3.0, see LICENSE
"""

import json
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
        """
        Instantiates an instance of an Urban Dictionary definition
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

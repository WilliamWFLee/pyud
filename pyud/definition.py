# -*- coding: utf-8 -*-
"""
pyud.definition
~~~~~~~~~~~~~~~

:copyright: 2020 William Lee
:license: GNU GPL v3.0, see LICENSE
"""

import json
from datetime import datetime as dt
from typing import Any, Dict, List, Union


class Definition:
    """
    Represents an Urban Dictionary definition
    """
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
        sound_urls: List[str],
        written_on: str,
        **attrs: Dict[str, Any],
    ):
        """
        Instantiates an instance of an Urban Dictionary definition

        This is usually done by using either one of `Client` or `AsyncClient`,
        and using one of the defined API wrapper methods/coroutines
        to retrieve definitions from the API.

        All of the fields in each of the definition objects
        returned from the API are required attributes on the class instance,
        except for `current_vote`, which is currently only an empty string.

        Attributes other than those required are added to the instance, 
        but they are not processed and are provided as is.
        """
        self.defid = defid
        self.word = word
        self.definition = definition
        self.author = author
        self.thumbs_up = thumbs_up
        self.thumbs_down = thumbs_down
        self.example = example
        self.permalink = permalink
        self.sound_urls = sound_urls

        # Parses the RFC 3339 timestring to a naive datetime object
        self.written_on = dt.strptime(written_on, "%Y-%m-%dT%H:%M:%S.%fZ")

        # Excess attributes are added
        for name, value in attrs.items():
            setattr(self, name, value)

# -*- coding: utf-8 -*-
"""
pyud.definition
~~~~~~~~~~~~~~~

:copyright: 2020 William Lee
:license: GNU GPL v3.0, see LICENSE
"""

from datetime import datetime as dt


class Definition:

    def __init__(self, *, defid: int, word: str, definition: str, author: str,
                 thumbs_up: int, thumbs_down: int, example: str,
                 permalink: str, written_on: str, **others):

        self.defid = defid
        self.word = word
        self.definition = definition
        self.author = author
        self.thumbs_up = thumbs_up
        self.thumbs_down = thumbs_down
        self.example = example
        self.permalink = permalink

        # Parses the RFC 3339 timestring to a naive datetime object
        self.written_on = dt.strptime("%Y-%m-%dT%H:%M:%S.%fZ")

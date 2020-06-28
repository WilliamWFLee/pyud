# -*- coding: utf-8 -*-
"""
pyud.client
~~~~~~~~~~~

:copyright: 2020 William Lee
:license: GNU GPL v3.0, see LICENSE
"""

import json
from typing import List, Optional, Union

from .definition import Definition

BASE_URL = "https://api.urbandictionary.com/v0/"
DEFINE_BY_TERM_URL = BASE_URL + "define?term={}"
DEFINE_BY_ID_URL = BASE_URL + "define?defid={}"
RANDOM_URL = BASE_URL + "random"


class ClientBase:
    """Base class for the Client and AsyncClient"""
    def _from_json(
        self, data: Union[str, bytes, bytearray]
    ) -> Optional[List[Definition]]:
        """Returns a list of Definitions from JSON

        The format of the JSON is a single array of definition objects
        under the key 'list' in the JSON document

        :param data: The definitions in JSON format
        :type data: Union[str, bytes, bytearray]
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

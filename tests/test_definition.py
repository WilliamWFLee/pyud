# -*- coding: utf-8 -*-
import pytest

import pyud

DATA = {
    "defid": 1,
    "word": "hello",
    "definition": "a very rude word",
    "author": "me",
    "thumbs_up": 13423,
    "thumbs_down": 43,
    "example": "hello [Karen]",
    "permalink": "http://hello.urbanup.com/14231",
    "sound_urls": [],
    "written_on": "2020-06-29T00:00:00.000Z",
}


def test_complete_definition():
    assert pyud.Definition(**DATA) is not None


def test_incomplete_definition():
    # No defid
    no_defid_data = DATA.copy()
    del no_defid_data["defid"]

    with pytest.raises(TypeError):
        definition = pyud.Definition(**no_defid_data)

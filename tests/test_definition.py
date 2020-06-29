# -*- coding: utf-8 -*-
import pyud


def test_complete_definition():
    data = {
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
    assert pyud.Definition(**data) is not None

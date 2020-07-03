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

INCORRECT_DATES = (
    "2020-06-29T00:00:00.000",  # Missing 'Z'
    "2020-06-29T00:00:00:000Z",  # : instead of . separating ms from s
    "2020-06-29T00:00:00Z",  # No millis
    "2020-06-29 00:00:00.000Z",  # Space instead of T
    "2020/06/29T00:00:00.000Z",  # Incorrect delimters for date
    "2020-06-29",  # Date-only
)

EXTRA_ATTRIBUTES = {
    "attribute1": 1,
    "attribute2": 2,
    "attribute3": "something",
    "attribute4": "another thing",
}


def test_complete_definition():
    assert pyud.Definition(**DATA) is not None


def test_incomplete_definition():
    for key in DATA:
        incomplete_data = DATA.copy()
        del incomplete_data[key]

        with pytest.raises(TypeError):
            pyud.Definition(**incomplete_data)


def test_incorrect_date_format():
    for date in INCORRECT_DATES:
        data = DATA.copy()
        data["written_on"] = date

        with pytest.raises(ValueError):
            pyud.Definition(**data)


def test_excess_attributes():
    data = DATA.copy()
    data = dict(data, **EXTRA_ATTRIBUTES)

    definition = pyud.Definition(**data)

    for key, value in EXTRA_ATTRIBUTES.items():
        assert getattr(definition, key) == value

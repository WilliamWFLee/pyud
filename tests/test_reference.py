# -*- coding: utf-8 -*-
import pytest

import pyud


@pytest.fixture
def reference():
    ud = pyud.Client()
    return pyud.Reference(ud, "hello")


@pytest.mark.incremental
class TestReference:
    def test_reference_word(self, reference):
        assert reference.word == "hello"

    def test_reference_define(self, reference):
        definitions = reference.define()
        for definition in definitions:
            assert definition.word.lower() == "hello"

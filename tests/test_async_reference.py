# -*- coding: utf-8 -*-
import pytest

import pyud


@pytest.fixture
def reference():
    ud = pyud.AsyncClient()
    return pyud.AsyncReference(ud, "hello")


@pytest.mark.incremental
class TestAsyncReference:
    @pytest.mark.asyncio
    async def test_reference_word(self, reference):
        assert reference.word == "hello"

    @pytest.mark.asyncio
    async def test_reference_define(self, reference):
        definitions = await reference.define()
        for definition in definitions:
            assert definition.word.lower() == "hello"

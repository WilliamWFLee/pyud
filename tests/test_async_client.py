# -*- coding: utf-8 -*-
import pytest

import pyud


@pytest.fixture
def client():
    return pyud.AsyncClient()


@pytest.mark.incremental
class TestAsyncClient:
    @pytest.mark.asyncio
    async def test_client(self, client):
        assert client

    @pytest.mark.asyncio
    async def test_client_define(self, client):
        assert await client.define('hello')
        assert await client.define('skadhfujahkduikfbresfvkayjfsrvued') is None

    @pytest.mark.asyncio
    async def test_client_from_id(self, client):
        assert (await client.from_id(2452556)).word == "Ping"
        assert await client.from_id(1) is None

    @pytest.mark.asyncio
    async def test_client_random(self, client):
        definitions = await client.random()
        assert definitions
        assert len(definitions) == 10

    @pytest.mark.asyncio
    async def test_client_random_limit(self, client):
        assert len(await client.random(limit=3)) == 3
        assert len(await client.random(limit=10)) == 10

    @pytest.mark.asyncio
    async def test_client_random_limit_gt_10(self, client):
        assert len(await client.random(limit=43)) == 43

# -*- coding: utf-8 -*-
import pytest

import pyud


@pytest.fixture
def client():
    return pyud.Client()


@pytest.mark.incremental
class TestClient:
    def test_client(self, client):
        assert client

    def test_client_define(self, client):
        assert client.define('hello')
        assert client.define('skadhfujahkduikfbresfvkayjfsrvued') is None

    def test_client_from_id(self, client):
        assert client.from_id(2452556).word == "Ping"
        assert client.from_id(1) is None

    def test_client_random(self, client):
        definitions = client.random()
        assert definitions
        assert len(definitions) == 10

    def test_client_random_limit(self, client):
        assert len(client.random(limit=3)) == 3
        assert len(client.random(limit=10)) == 10

    @pytest.mark.xfail
    def test_client_random_limit_gt_10(self, client):
        assert len(client.random(limit=43)) == 43

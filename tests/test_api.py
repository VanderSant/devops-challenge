""" Api main test."""
import json


def test_main(client):
    """Main route test."""
    response = client.get("/")
    res = json.loads(response.data.decode("utf-8"))
    print(res)
    assert res["App Test"] == "Alive"


def test_status(client):
    """Status route test."""
    response = client.get("/healthcheck")
    res = json.loads(response.data.decode("utf-8"))
    print(res)
    assert res["Status"] == "heart beating steady and strong"


def test_status_2(client):
    """Status route test."""
    response = client.get("/healthcheck")
    res = json.loads(response.data.decode("utf-8"))
    print(res)
    assert res["Status"] == "heart beating steady and strong"

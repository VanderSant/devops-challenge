""" Client provider to test."""
import pytest
from src.application import app


@pytest.fixture
def client():
    """Configures the app for testing

    Sets app config variable ``TESTING`` to ``True``

    :return: App for testing
    """

    app.config["TESTING"] = True
    api_client = app.test_client()

    yield api_client

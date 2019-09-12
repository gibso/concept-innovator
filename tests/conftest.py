import pytest
from orpheus_specifier import create_app
import os


@pytest.fixture
def app():
    app = create_app({
        'TESTING': True,
        'MAX_FACTS_PER_RELATION': 1,
        'VALID_FACT_LANGUAGES': 'de,en',
        'CONCEPTNET_HOST': 'api.conceptnet.io'
    })

    yield app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()

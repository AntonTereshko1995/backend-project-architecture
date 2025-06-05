import pytest

from src.app.controllers.key_value_controller import KeyValueController
from src.app.create_flask_app import create_flask_app
from src.infa.db.loggers.logger_default import LoggerDefault
from test.conftest import fixture_key_value

logger = LoggerDefault()

@pytest.fixture
def app_flask_app():
    app = create_flask_app(logger)
    app.config.update({
        "TESTING": True,
    })
    yield app

@pytest.fixture
def client_flask_app(app_flask_app):
    return app_flask_app.test_client()

@pytest.mark.skip(reason="Test requires database connection")
def test_request_key_value(client_flask_app, fixture_key_value):
    input_data = {
        "key": fixture_key_value["key"],
        "value": fixture_key_value["value"],
    }

    response = client_flask_app.post("/v1/create/", json=input_data)

    assert fixture_key_value["key"].encode() in response.data
    assert fixture_key_value["value"].encode() in response.data

@pytest.mark.skip(reason="Test requires database connection")
def test_request_missing_value_error(client_flask_app, fixture_key_value):
    input_data = {
        "key": fixture_key_value["key"],
    }

    response = client_flask_app.post("/v1/create/", json=input_data)
    assert b"Missing value" in response.data

@pytest.mark.skip(reason="Test requires database connection")
def test_request_wrong_url_error(client_flask_app, fixture_key_value):
    input_data = {
        "key": fixture_key_value["key"],
        "value": fixture_key_value["value"],
    }

    response = client_flask_app.post("/v1/creat/", json=input_data)
    assert b"The requested URL was not found on the server" in response.data

@pytest.mark.skip(reason="Test requires database connection")
def test_request_500_status_code(client_flask_app, mocker, fixture_key_value):
    blueprint_mock = mocker.patch.object(KeyValueController, "get_key_value_info")
    blueprint_mock.side_effect = Exception('Unexpected error!')

    input_data = {
        "key": fixture_key_value["key"],
        "value": fixture_key_value["value"],
    }

    response = client_flask_app.post("/v1/create/", json=input_data)
    assert b'"status_code":500' in response.data

import pytest
from unittest import mock
from src.interactor.errors.error_classes import KeyAlreadyExistsError
from test.conftest import fixture_key_value
from src.app.controllers.key_value_controller import KeyValueController
from src.interactor.dtos.key_value_dto import KeyValueInputDto
from src.interactor.interfaces.loggers.logger_interface import ILogger

@pytest.fixture
def fixture_logger(mocker):
    return mocker.patch.object(ILogger, "log_info")

def test_create_key_value_controller(mocker, monkeypatch, fixture_logger, fixture_key_value):
    repository_mock = mocker.patch("src.app.controllers.key_value_controller.KeyValueController")
    presenter_mock = mocker.patch("src.app.presenters.key_value_presenter.KeyValuePresenter")
    use_case_mock = mocker.patch("src.interactor.use_cases.key_value_use_case.KeyValueUseCase")

    use_case_result = {
        "key": fixture_key_value["key"],
        "value": fixture_key_value["value"],
    }

    use_case_instance = use_case_mock.return_value
    use_case_instance.execute.return_value = use_case_result

    inputs = {
        "key": fixture_key_value["key"],
        "value": fixture_key_value["value"],
    }

    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    controller = KeyValueController(fixture_logger)

    with pytest.raises(KeyAlreadyExistsError) as exception_info:
        controller.create(inputs)

    key_value = fixture_key_value["key"]
    assert str(exception_info.value) == f"Key '{key_value}' already exists."

    controller.delete(fixture_key_value["key"])

def test_missing_inputs(fixture_logger, fixture_key_value):
    controller = KeyValueController(fixture_logger)

    # Missing key
    fake_inputs = {
        "value": fixture_key_value["value"],
    }

    with pytest.raises(ValueError) as exception_info:
        controller.create(fake_inputs)

    assert str(exception_info.value) == "Missing key"

    # Missing value
    fake_inputs = {
        "key": fixture_key_value["key"],
    }

    with pytest.raises(ValueError) as exception_info:
        controller.create(fake_inputs)

    assert str(exception_info.value) == "Missing value"
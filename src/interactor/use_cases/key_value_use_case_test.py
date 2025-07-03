from unittest.mock import patch
import pytest
from src.interactor.dtos.key_value_dto import KeyValueInputDto, KeyValueOutputDto
from src.interactor.errors.error_classes import NotCreatedError
from src.interactor.interfaces.loggers.logger_interface import ILogger
from src.interactor.interfaces.presenters.key_value_presenter_interface import IKeyValuePresenter
from src.interactor.interfaces.repositories.key_value_repository_interface import IKeyValueRepository
from src.interactor.use_cases.key_value_use_case import KeyValueUseCase
from test.conftest import fixture_key_value


@pytest.fixture
def repository(mocker, fixture_key_value):
    repository = mocker.patch.object(IKeyValueRepository, "create")
    repository.create.return_value = {
        "key": fixture_key_value["key"],
        "value": fixture_key_value["value"],
    }
    return repository

@pytest.fixture
def presenter(mocker):
    return mocker.patch.object(IKeyValuePresenter, "create")

@pytest.fixture
def logger(mocker):
    return mocker.patch.object(ILogger, "log_info")

@patch("src.interactor.validations.key_value_validator.KeyValueValidator")
def test_create_user(validator, repository, presenter, logger, fixture_key_value):
    presenter.present.return_value = "Test output"

    input_dto = KeyValueInputDto(
        key=fixture_key_value["key"],
        value=fixture_key_value["value"],
    )

    use_case = KeyValueUseCase(repository, presenter, logger)

    assert use_case.execute(input_dto) == presenter.present.return_value

    validator.assert_called_once_with(input_dto.to_dict())
    validator_instance = validator.return_value
    validator_instance.validate.assert_called_once()

    repository.create.assert_called_once_with(
        fixture_key_value["key"],
        fixture_key_value["value"],
    )

    logger.log_info.assert_called_once_with("Key created successfully")

    output_dto = KeyValueOutputDto(repository.create.return_value)
    presenter.present.assert_called_once_with(output_dto)

    # Testing None return value from repository
    repository.create.return_value = None

    with pytest.raises(NotCreatedError) as exception:
        use_case.execute(input_dto)

    name = f"{fixture_key_value['key']} {fixture_key_value['value']}"
    assert str(exception.value) == f"Failed to create key '{name.capitalize()}'"
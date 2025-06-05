from src.app.presenters.key_value_presenter import KeyValuePresenter
from src.interactor.dtos.key_value_dto import KeyValueOutputDto
from test.conftest import fixture_key_value

def test_create_user_presenter(fixture_key_value):
    presenter = KeyValuePresenter()
    output_dto = KeyValueOutputDto(fixture_key_value["key"], fixture_key_value["value"])
    expected_response = {
        "key": fixture_key_value["key"],
        "value": fixture_key_value["value"],
    }

    assert presenter.present(output_dto) == expected_response
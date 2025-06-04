from typing import Dict
from src.interactor.dtos.key_value_dto import KeyValueOutputDto
from src.interactor.presenters.key_value_presenter_interface import IKeyValuePresenter

class KeyValuePresenter(IKeyValuePresenter):

    def present(cls, output_dto: KeyValueOutputDto) -> Dict:
        return {
            "key": output_dto.key,
            "value": output_dto.value,
        }
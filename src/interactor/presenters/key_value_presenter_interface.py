from abc import ABC, abstractmethod
from typing import Dict
from src.interactor.dtos.key_value_dto import KeyValueOutputDto

class IKeyValuePresenter(ABC):

    @abstractmethod
    def present(self, output_dto: KeyValueOutputDto) -> Dict:
        pass

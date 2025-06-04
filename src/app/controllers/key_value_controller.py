from typing import Dict
from src.app.interfaces.flask_controller_interface import IFlaskController
from src.app.presenters.key_value_presenter import KeyValuePresenter
from src.infa.db.repositories.key_value_repository import KeyValueRepository
from src.interactor.dtos.key_value_dto import KeyInputDto, KeyValueInputDto
from src.interactor.interfaces.loggers.logger_interface import ILogger
from src.interactor.use_cases.key_value_use_case import KeyValueUseCase

class KeyValueController(IFlaskController):

    def __init__(self, logger: ILogger) -> None:
        self.__logger = logger

    def create(self, json_input) -> Dict:
        repository = KeyValueRepository()
        presenter = KeyValuePresenter()
        logger = self.__logger
        use_case = KeyValueUseCase(repository, presenter, logger)
        input_dto = self.get_key_value_info(json_input)
        return use_case.create(input_dto)
    
    def delete(self, key) -> Dict:
        repository = KeyValueRepository()
        presenter = KeyValuePresenter()
        logger = self.__logger
        use_case = KeyValueUseCase(repository, presenter, logger)
        input_dto = KeyInputDto(key)
        return use_case.delete(input_dto)
    
    def get(self, key) -> Dict:
        repository = KeyValueRepository()
        presenter = KeyValuePresenter()
        logger = self.__logger
        use_case = KeyValueUseCase(repository, presenter, logger)
        input_dto = KeyInputDto(key)
        return use_case.get(input_dto)
    
    def update(self, json_input) -> Dict:
        repository = KeyValueRepository()
        presenter = KeyValuePresenter()
        logger = self.__logger
        use_case = KeyValueUseCase(repository, presenter, logger)
        input_dto = self.get_key_value_info(json_input)
        return use_case.update(input_dto)

    def get_key_value_info(self, json) -> KeyValueInputDto:
        if "key" in json:
            key = json["key"]
        else:
            raise ValueError("Missing key")

        if "value" in json:
            value = json["value"]
        else:
            raise ValueError("Missing value")

        return KeyValueInputDto(key, value)
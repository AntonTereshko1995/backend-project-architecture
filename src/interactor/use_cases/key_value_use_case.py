from typing import Dict
from src.interactor.dtos.key_value_dto import KeyInputDto, KeyValueInputDto, KeyValueOutputDto
from src.interactor.interfaces.loggers.logger_interface import ILogger
from src.interactor.interfaces.presenters.key_value_presenter_interface import IKeyValuePresenter
from src.interactor.interfaces.repositories.key_value_repository_interface import IKeyValueRepository
from src.interactor.validations.key_validator import KeyValidator
from src.interactor.validations.key_value_validator import KeyValueValidator

class KeyValueUseCase:

    def __init__(
        self,
        repository: IKeyValueRepository,
        presenter: IKeyValuePresenter,
        logger: ILogger
    ) -> None:
        self.__repository = repository
        self.__presenter = presenter
        self.__logger = logger

    def create(self, input_dto: KeyValueInputDto) -> Dict:
        validator = KeyValueValidator(input_dto.to_dict())
        validator.validate()

        self.__repository.create(input_dto.key, input_dto.value)
        self.__logger.log_info("Key created successfully")

        output_dto = KeyValueOutputDto(input_dto.key, input_dto.value)
        presenter_response = self.__presenter.present(output_dto)
        return presenter_response
    
    def get(self, input_dto: KeyInputDto) -> Dict:
        validator = KeyValidator(input_dto.to_dict())
        validator.validate()

        value = self.__repository.get(input_dto.key)
        self.__logger.log_info("Key got successfully")

        output_dto = KeyValueOutputDto(input_dto.key, value)
        presenter_response = self.__presenter.present(output_dto)
        return presenter_response
    
    def delete(self, input_dto: KeyInputDto) -> Dict:
        validator = KeyValidator(input_dto.to_dict())
        validator.validate()

        self.__repository.delete(input_dto.key)
        self.__logger.log_info("Key deleted successfully")

        output_dto = KeyValueOutputDto(input_dto.key, "")
        presenter_response = self.__presenter.present(output_dto)
        return presenter_response
    
    def update(self, input_dto: KeyValueInputDto) -> Dict:
        validator = KeyValueValidator(input_dto.to_dict())
        validator.validate()

        self.__repository.update(input_dto.key, input_dto.value)
        self.__logger.log_info("Key updated successfully")

        output_dto = KeyValueOutputDto(input_dto.key, input_dto.value)
        presenter_response = self.__presenter.present(output_dto)
        return presenter_response
from typing import Dict
from .base_validator import BaseValidator
from .base_schema import key_schema, value_schema

class KeyValidator(BaseValidator):

    def __init__(self, input_data: Dict) -> None:
        super().__init__(input_data)

        self.__schema = {
            "key": key_schema,
        }

    def validate(self) -> None:
        super().verify(self.__schema)

from abc import ABC, abstractmethod
from typing import Dict

class IFlaskController(ABC):

    @abstractmethod
    def create(self, input_json) -> Dict:
        pass

    @abstractmethod
    def delete(self, input_json) -> Dict:
        pass

    @abstractmethod
    def get(self, input_json) -> Dict:
        pass

    @abstractmethod
    def update(self, input_json) -> Dict:
        pass
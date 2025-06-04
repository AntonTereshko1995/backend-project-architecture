from abc import ABC, abstractmethod
from typing import Optional


class IKeyValueRepository(ABC):

    @abstractmethod
    def create(self, key: str, value: str):
        pass

    @abstractmethod
    def get(self, key: str) -> Optional[str]:
        pass

    @abstractmethod
    def delete(self, key: str):
        pass

    @abstractmethod
    def update(self, key: str, value: str):
        pass
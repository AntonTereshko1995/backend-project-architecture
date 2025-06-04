from abc import ABC, abstractmethod
from typing import Optional

class IKeyValueRepository(ABC):

    @abstractmethod
    def create(self, key: str, value: str) -> Optional[str]:
        pass

    @abstractmethod
    def get(self, key: str) -> Optional[str]:
        pass

    @abstractmethod
    def remove(self, key: str) -> Optional[str]:
        pass

    @abstractmethod
    def update(self, key: str, value: str) -> Optional[str]:
        pass

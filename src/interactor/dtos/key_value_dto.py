from dataclasses import asdict, dataclass
from typing import Dict

@dataclass
class KeyValueInputDto:
    key: str
    value: str

    def to_dict(self) -> Dict:
        return asdict(self)
    
@dataclass
class KeyInputDto:
    key: str

    def to_dict(self) -> Dict:
        return asdict(self)

@dataclass
class KeyValueOutputDto:
    key: str
    value: str

    def to_dict(self) -> Dict:
        return asdict(self)

@dataclass
class KeyOutputDto:
    key: str

    def to_dict(self) -> Dict:
        return asdict(self)
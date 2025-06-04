import json
from typing import Optional
import redis
from src.infa.db.settings.connection import RedisClientFactory
from src.interactor.errors.error_classes import KeyAlreadyExistsError, KeyNotFoundError
from src.interactor.interfaces.repositories.key_value_repository_interface import IKeyValueRepository

class KeyValueRepository(IKeyValueRepository):

    def __init__(self, prefix: str = "kv:"):
        self.redis = RedisClientFactory().get_client()
        self.prefix = prefix

    def create(self, key: str, value: str):
        full_key = self._format_key(key)
        if self.redis.exists(full_key):
            raise KeyAlreadyExistsError(f"Key '{key}' already exists.")
        self.redis.set(full_key, json.dumps(value))

    def get(self, key: str) -> Optional[str]:
        full_key = self._format_key(key)
        raw = self.redis.get(full_key)
        if raw is None:
            raise KeyNotFoundError(f"Key '{key}' not found.")
        return json.loads(raw)
            
    def delete(self, key: str):
        full_key = self._format_key(key)
        if not self.redis.exists(full_key):
            raise KeyNotFoundError(f"Key '{key}' not found.")
        self.redis.delete(full_key)
            
    def update(self, key: str, value: str):
        full_key = self._format_key(key)
        if not self.redis.exists(full_key):
            raise KeyNotFoundError(f"Key '{key}' not found.")
        self.redis.set(full_key, json.dumps(value))

    def _format_key(self, key: str) -> str:
        return f"{self.prefix}{key}"
import redis
from configs import config as config_app

class RedisClientFactory:
    _client = None

    @classmethod
    def get_client(cls):
        if cls._client is None:
            cls._client = redis.Redis(
                host=config_app.REDIS_HOST,
                port=config_app.REDIS_PORT,
                db=config_app.REDIS_DB,
                password=config_app.REDIS_PASSWORD,
                decode_responses=True)
        return cls._client
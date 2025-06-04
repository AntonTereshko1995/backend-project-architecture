import os
from dotenv import load_dotenv


if "redis" in os.environ:
    load_dotenv(dotenv_path="configs/docker.env")
else:
    load_dotenv(dotenv_path="configs/debug.env")


REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_DB = int(os.getenv("REDIS_DB", 0))
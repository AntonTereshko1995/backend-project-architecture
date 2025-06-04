import os
from dotenv import load_dotenv


load_dotenv()  # take environment variables from .env

# DB_USER = os.getenv("DATABASE_USER")
# DB_PASS = os.getenv("DATABASE_PASSWORD")
# DB_NAME = os.getenv("DATABASE_NAME")
# DB_HOST = os.getenv("DATABASE_HOST")
# DB_PORT = os.getenv("DATABASE_PORT")
# DB_DRIVER = "postgresql+psycopg2"


DB_URI = "sqlite:///test_the_secret_house.db"

import os

from dotenv import load_dotenv

BASE_SAVE_DIR = os.path.join(os.getcwd(), "temp")

load_dotenv()

config: dict = os.environ

POSTGRES_URI = config["POSTGRES_URI"]
REDIS_URI = config["REDIS_URI"]
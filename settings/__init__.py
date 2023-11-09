from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

import os

# 👇️ /home/borislav/Desktop/bobbyhadz_python/main.py
print(__file__)

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


@lru_cache
def get_settings():
    return Settings()


class Settings(BaseSettings):
    datastore: str = None
    model_config = SettingsConfigDict(env_file=os.path.join(ROOT_DIR, ".env"))

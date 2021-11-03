import os
import logging
from pydantic import BaseSettings, AnyUrl
from functools import lru_cache

log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
  environment: str = os.getenv("ENVIRONMENT", "dev")
  testing: bool = os.getenv("TESTING", False)
  database_url: AnyUrl = os.getenv("DATABASE_URL")


@lru_cache()
def get_settings() -> BaseSettings:
  log.info("Loading config settings from the environment...")
  return Settings()

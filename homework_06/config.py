from os import getenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DEFAULT_DB_URL = "postgresql://username:passwd@0.0.0.0:5432/blog"

SQLALCHEMY_DATABASE_URI = getenv(
    "SQLALCHEMY_DATABASE_URI",
    DEFAULT_DB_URL,
)


class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_ECHO = False
    SECRET_KEY = "bcd46b310f2745cf6ae662cffd5dfb7f19f8322d694944448f88aea7d0e4f606"


class DevelopmentConfig(Config):
    SQLALCHEMY_ECHO = False


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    TESTING = False
    DEBUG = False

from pathlib import Path

from app.models.settings import Settings
from vcore.backend.core.env import load_env


def get_settings(env_file_path: Path | str, version: str | None = None) -> Settings:
    """
    Loads settings from env_file_path and version.
    """
    load_env(env_file_path)
    return Settings(VERSION=version)

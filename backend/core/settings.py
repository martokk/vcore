from pathlib import Path

from backend.core.env import load_env
from backend.models.settings import PythonFastAPIBaseSettings


def get_settings(
    settings_cls: type[PythonFastAPIBaseSettings],
    env_file_path: Path | str,
    version: str | None = None,
) -> PythonFastAPIBaseSettings:
    """
    Loads settings from env_file_path and version.
    """
    load_env(env_file_path)
    return settings_cls(VERSION=version)

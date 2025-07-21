import os
from pathlib import Path

from dotenv import load_dotenv as _load_dotenv


def find_env_file_path(project_path: Path, env_file_path: Path | None = None) -> Path:
    """
    Find the environment variables file in the project path.
    """

    env_file_from_env_var = os.getenv("ENV_FILE_PATH")

    possible_paths = [
        env_file_path,
        Path(env_file_from_env_var) if env_file_from_env_var else None,
        project_path / "data" / ".env",
        project_path / "vcore" / "data" / ".env",
    ]
    for possible_env_file in possible_paths:
        if possible_env_file and possible_env_file.exists():
            return possible_env_file
    raise FileNotFoundError("No environment variables file found")


def load_env_file(env_file_path: Path | str) -> None:
    """
    Load the environment variables from the given file path.

    Args:
        env_file_path: The path to the environment variables file.
    """
    _load_dotenv(dotenv_path=Path(env_file_path))
    print(f"Loaded ENV_FILE: {env_file_path}")

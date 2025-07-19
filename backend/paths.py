# PROJECT STRUCTURE
import os
from pathlib import Path

from backend.core.settings import get_settings
from backend.models.settings import PythonFastAPIBaseSettings


def convert_relative_path_to_absolute(path: str) -> Path:  # TODO: Move to backend.paths
    if str(path).startswith("/app/"):
        joined_path = f"{PROJECT_PATH}{path}"
        return Path(joined_path)
    if str(path).startswith("app/"):
        joined_path = f"{PROJECT_PATH}/{path}"
        return Path(joined_path)
    return Path(path)


# Project Path
PROJECT_PATH = Path(os.path.dirname(os.path.abspath(__file__))).parent

# MAIN PATHS
APP_PATH = PROJECT_PATH / "app"
VCORE_PATH = PROJECT_PATH / "vcore"

# Folders
DATA_PATH = PROJECT_PATH / "data"
FRONTEND_PATH = PROJECT_PATH / "frontend"
VCORE_FRONTEND_PATH = VCORE_PATH / "frontend"

# Frontend Folder
STATIC_PATH = FRONTEND_PATH / "static"
VCORE_STATIC_PATH = VCORE_FRONTEND_PATH / "static"

EMAIL_TEMPLATES_PATH = FRONTEND_PATH / "email-templates"
VCORE_EMAIL_TEMPLATES_PATH = VCORE_FRONTEND_PATH / "email-templates"

TEMPLATES_PATH = FRONTEND_PATH / "templates"
VCORE_TEMPLATES_PATH = VCORE_FRONTEND_PATH / "templates"

# Data Folder
LOGS_PATH = DATA_PATH / "logs"
CACHE_PATH = DATA_PATH / "cache"
UPLOAD_PATH = DATA_PATH / "uploads"

# Job Queue Paths
JOB_LOGS_PATH = LOGS_PATH / "jobs"

# ENV File
ENV_FILE_FROM_ENV = os.environ.get("ENV_FILE")

ENV_FILES_PATHS = [
    Path(ENV_FILE_FROM_ENV) if ENV_FILE_FROM_ENV else None,
    PROJECT_PATH / ENV_FILE_FROM_ENV if ENV_FILE_FROM_ENV else None,
    DATA_PATH / ".env",
]
ENV_FILE = None

if not ENV_FILE:
    ENV_FILE = VCORE_PATH / "data" / ".env"

for env_file_path in ENV_FILES_PATHS:
    if env_file_path and env_file_path.exists():
        print(f"Found ENV file at {env_file_path}")
        ENV_FILE = env_file_path
        break
print(f"ENV_FILE: {ENV_FILE}")

# Load ENV File - Needed for Settings
settings = get_settings(settings_cls=PythonFastAPIBaseSettings, env_file_path=str(ENV_FILE))

# Files
DEFAULT_DATABASE_FILE = DATA_PATH / "database.sqlite3"
DB_URL = settings.DB_URL or f"sqlite:///{DEFAULT_DATABASE_FILE}"
PYPROJECT_FILE = PROJECT_PATH / "pyproject.toml"
LOG_FILE = LOGS_PATH / "log.log"
ERROR_LOG_FILE = LOGS_PATH / "error_log.log"


# Job Queue Paths
HUEY_DEFAULT_DB_PATH = convert_relative_path_to_absolute(settings.HUEY_DEFAULT_SQLITE_PATH)
HUEY_RESERVED_DB_PATH = convert_relative_path_to_absolute(settings.HUEY_RESERVED_SQLITE_PATH)
HUEY_DEFAULT_LOG_PATH = convert_relative_path_to_absolute(settings.HUEY_DEFAULT_LOG_PATH)
HUEY_RESERVED_LOG_PATH = convert_relative_path_to_absolute(settings.HUEY_RESERVED_LOG_PATH)
HUEY_DEFAULT_PID_FILE = HUEY_DEFAULT_LOG_PATH.with_suffix(".pid")
HUEY_RESERVED_PID_FILE = HUEY_RESERVED_LOG_PATH.with_suffix(".pid")

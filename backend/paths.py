# PROJECT STRUCTURE
from pathlib import Path

from backend import PROJECT_PATH, settings

if not PROJECT_PATH:
    raise RuntimeError(
        "VCore is not setup. Call vcore_setup() before importing other backend modules."
    )


def convert_relative_path_to_absolute(path: str) -> Path:  # TODO: Move to backend.paths
    if str(path).startswith("/app/"):
        joined_path = f"{PROJECT_PATH}{path}"
        return Path(joined_path)
    if str(path).startswith("app/"):
        joined_path = f"{PROJECT_PATH}/{path}"
        return Path(joined_path)
    return Path(path)


# Files
PYPROJECT_FILE = PROJECT_PATH / "pyproject.toml"

# MAIN PATHS
APP_PATH = PROJECT_PATH / "app"
VCORE_PATH = PROJECT_PATH / "vcore"
DATA_PATH = PROJECT_PATH / "data"
FRONTEND_PATH = PROJECT_PATH / "frontend"
STATIC_PATH = FRONTEND_PATH / "static"

# VCORE PATHS
VCORE_FRONTEND_PATH = VCORE_PATH / "frontend"
VCORE_STATIC_PATH = VCORE_FRONTEND_PATH / "static"
VCORE_EMAIL_TEMPLATES_PATH = VCORE_FRONTEND_PATH / "email-templates"
VCORE_TEMPLATES_PATH = VCORE_FRONTEND_PATH / "templates"

# Data Folder
DATA_PATH = PROJECT_PATH / "data"
LOGS_PATH = DATA_PATH / "logs"
CACHE_PATH = DATA_PATH / "cache"
UPLOAD_PATH = DATA_PATH / "uploads"

# Database
DEFAULT_DATABASE_FILE = DATA_PATH / "database.sqlite3"
DB_URL = settings.DB_URL or f"sqlite:///{DEFAULT_DATABASE_FILE}"

# Logs
LOG_FILE = DATA_PATH / "logs" / "log.log"
ERROR_LOG_FILE = DATA_PATH / "logs" / "error_log.log"

# Frontend Folders
FRONTEND_PATH = PROJECT_PATH / "frontend"
STATIC_PATH = FRONTEND_PATH / "static"
EMAIL_TEMPLATES_PATH = FRONTEND_PATH / "email-templates"
TEMPLATES_PATH = FRONTEND_PATH / "templates"

# Job Queue Paths
JOB_LOGS_PATH = LOGS_PATH / "jobs"
HUEY_DEFAULT_DB_PATH = convert_relative_path_to_absolute(
    settings.HUEY_DEFAULT_SQLITE_PATH
)
HUEY_RESERVED_DB_PATH = convert_relative_path_to_absolute(
    settings.HUEY_RESERVED_SQLITE_PATH
)
HUEY_DEFAULT_LOG_PATH = convert_relative_path_to_absolute(
    settings.HUEY_DEFAULT_LOG_PATH
)
HUEY_RESERVED_LOG_PATH = convert_relative_path_to_absolute(
    settings.HUEY_RESERVED_LOG_PATH
)
HUEY_DEFAULT_PID_FILE = HUEY_DEFAULT_LOG_PATH.with_suffix(".pid")
HUEY_RESERVED_PID_FILE = HUEY_RESERVED_LOG_PATH.with_suffix(".pid")

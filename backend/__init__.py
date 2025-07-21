from pathlib import Path

from loguru import logger as loguru_logger

from backend.core.logger import setup_logger
from backend.core.settings import VCoreBaseSettings, get_settings


PROJECT_PATH: Path
settings: VCoreBaseSettings
logger = loguru_logger


def vcore_setup(
    project_path: Path,
) -> None:
    """Setup vcore - MUST be called before importing other backend modules."""
    global PROJECT_PATH, settings, logger

    PROJECT_PATH = project_path
    settings = get_settings(
        project_path=PROJECT_PATH,
        settings_cls=VCoreBaseSettings,
    )
    logger = setup_logger(
        error_log_file_path=PROJECT_PATH / "data" / "logs" / "error_log.log",
        log_file_path=PROJECT_PATH / "data" / "logs" / "log.log",
        log_level=settings.LOG_LEVEL,
    )

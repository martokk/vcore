from pathlib import Path
from typing import TYPE_CHECKING

from loguru import logger as _logger


if TYPE_CHECKING:
    from loguru import Logger

LOGGER: "Logger"


def setup_logger(
    error_log_file_path: Path,
    log_file_path: Path,
    log_level: str,
) -> "Logger":
    """Configure and return the application logger."""
    global LOGGER

    # Remove existing default logger to avoid duplicate logs
    _logger.remove()

    # Configure loggers for file output
    _logger.add(
        log_file_path,
        filter=lambda record: record["extra"].get("name") == "logger",
        level=log_level,
        rotation="10 MB",
    )
    _logger.add(
        error_log_file_path,
        filter=lambda record: record["extra"].get("name") == "logger",
        level="ERROR",
        rotation="10 MB",
    )
    # Create bound logger
    logger = _logger.bind(name="logger")
    logger.info(f"Log level set by .env to '{log_level}'")

    LOGGER = logger

    return logger


def get_logger() -> "Logger":
    """Get the logger."""
    global LOGGER
    if not LOGGER:
        raise ValueError("Logger not set")
    return LOGGER

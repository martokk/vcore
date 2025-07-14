from pathlib import Path
from typing import Any

from loguru import logger as _logger


def setup_logger(
    error_log_file_path: Path,
    log_file_path: Path,
    log_level: str,
) -> Any:
    """Configure and return the application logger."""

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

    return logger

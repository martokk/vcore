from backend.core.logger import setup_logger
from backend.models.settings import PythonFastAPIBaseSettings
from backend.paths import ERROR_LOG_FILE, LOG_FILE


settings = PythonFastAPIBaseSettings()

logger = setup_logger(
    error_log_file_path=ERROR_LOG_FILE,
    log_file_path=LOG_FILE,
    log_level=settings.LOG_LEVEL,
)

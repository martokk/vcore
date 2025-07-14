from vcore.backend.core.logger import setup_logger
from vcore.backend.models.settings import PythonFastAPIBaseSettings
from vcore.backend.paths import ERROR_LOG_FILE, LOG_FILE


settings = PythonFastAPIBaseSettings()

logger = setup_logger(
    error_log_file_path=ERROR_LOG_FILE,
    log_file_path=LOG_FILE,
    log_level=settings.LOG_LEVEL,
)

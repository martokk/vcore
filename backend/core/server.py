import uvicorn

from backend import logger
from backend.core.settings import VCoreBaseSettings


def start_server(settings: VCoreBaseSettings) -> None:
    """
    Start Uvicorn server using the configuration from settings.
    """
    logger.debug("Starting uvicorn server...")
    uvicorn.run(
        settings.UVICORN_ENTRYPOINT,
        host=settings.SERVER_HOST,
        port=settings.SERVER_PORT,
        log_level=settings.LOG_LEVEL.lower(),
        reload=False,
        workers=1,
        app_dir="",
    )

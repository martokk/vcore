from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from sqlmodel import Session


from vcore.backend.core.db import get_db_context, initialize_tables_and_initial_data
from vcore.backend.jobs.execute_scheduler import run_on_start_schedulers
from vcore.backend.services import notify
from vcore.backend.services.job_queue import (
    start_huey_consumers_on_start,
)


# def run_playground_app():
#     subprocess.run(
#         [
#             "uvicorn",
#             "app.core.phidata_playground:app",
#             "--host",
#             "127.0.0.1",
#             "--port",
#             "7777",
#             "--reload",
#         ]
#     )


async def startup_event(db: Session | None = None) -> None:
    """
    Event handler that gets called when the application starts.
    Logs application start and creates database and tables if they do not exist.

    Args:
        db (Session): Database session.
    """
    logger.info("--- Start FastAPI ---")
    if settings.NOTIFY_ON_START:
        await notify.notify(text=f"{settings.PROJECT_NAME}('{settings.ENV_NAME}') started.")

    # Initialize database and tables if they do not exist
    if db is None:
        with get_db_context() as db:
            await initialize_tables_and_initial_data(db=db, sqlmodel_create_all=True)
    else:
        await initialize_tables_and_initial_data(db=db, sqlmodel_create_all=True)

    # Run on_start job schedulers
    run_on_start_schedulers()

    # Ensure Huey consumers are running at startup
    await start_huey_consumers_on_start()


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    # Startup
    await startup_event()

    yield

    # Shutdown
    logger.info("--- Shutdown FastAPI ---")


# Initialize FastAPI App
app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_PREFIX}/openapi.json",
    debug=settings.DEBUG,
    lifespan=lifespan,
)

# Include routers
app.include_router(api_router, prefix=settings.API_V1_PREFIX)
app.include_router(views_router)

# Mount static and uploads directories
STATIC_PATH.mkdir(parents=True, exist_ok=True)
app.mount("/static", StaticFiles(directory=STATIC_PATH))

VCORE_STATIC_PATH.mkdir(parents=True, exist_ok=True)
app.mount("/vcore/static", StaticFiles(directory=VCORE_STATIC_PATH))

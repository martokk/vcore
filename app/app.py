from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from sqlmodel import Session

from app.templating.env import inject_app_templating_env
from backend import logger, settings
from backend.core.db import get_db_context, initialize_tables_and_initial_data
from backend.core.hooks import register_hook
from backend.jobs.execute_scheduler import run_on_start_schedulers
from backend.paths import STATIC_PATH
from backend.routes.api import vcore_api_router
from backend.routes.views import vcore_views_router
from backend.scripts.example import ScriptExample
from backend.services import notify
from backend.services.job_queue import (
    start_huey_consumers_on_start,
)
from backend.services.scripts import register_script


# def run_playground_app():
#     subprocess.run(
#         [
#             "uvicorn",
#             "backend.core.phidata_playground:app",
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
    init_app_specific_data_func = (
        None  # Replace with app.logic.init_db:initialize_project_specific_data function
    )
    if db is None:
        with get_db_context() as db:
            await initialize_tables_and_initial_data(
                db=db,
                sqlmodel_create_all=True,
                init_app_specific_data_func=init_app_specific_data_func,
            )
    else:
        await initialize_tables_and_initial_data(
            db=db, sqlmodel_create_all=True, init_app_specific_data_func=init_app_specific_data_func
        )

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


# Register Hooks
register_hook("inject_app_templating_env", inject_app_templating_env)

# Register Scripts
register_script("ScriptExample", ScriptExample)

# Initialize FastAPI App
app = FastAPI(
    title="dummy",
    debug=True,
    lifespan=lifespan,
)

# Include routers
app.include_router(vcore_api_router, prefix="/api/v1")
app.include_router(vcore_views_router)

# Mount static files
# STATIC_PATH.mkdir(parents=True, exist_ok=True)
app.mount("/vcore/static", StaticFiles(directory=STATIC_PATH))

# # VCORE_STATIC_PATH.mkdir(parents=True, exist_ok=True)
# app.mount("/vcore/static", StaticFiles(directory=VCORE_STATIC_PATH))

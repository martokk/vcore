from collections.abc import Awaitable, Callable, Generator
from contextlib import contextmanager
from typing import Any

from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool
from sqlmodel import Session, SQLModel, create_engine

from backend import crud, logger, models, paths, settings


engine = create_engine(
    url=paths.DB_URL,
    echo=settings.DATABASE_ECHO,
    connect_args={
        "check_same_thread": "sqlite" not in paths.DB_URL
    },  # =False for SQLite / NOT for PostgreSQL
    pool_pre_ping=True,
    poolclass=QueuePool,
    pool_size=20,
    max_overflow=30,
    pool_timeout=60,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=Session)


def get_db() -> Generator[Session, None, None]:
    """
    A generator function that creates a new database session, used for FastAPI dependency injection.

    Yields:
        db: A new database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@contextmanager
def get_db_context() -> Generator[Session, None, None]:
    """
    A context manager that creates a new database session, used outside of FastAPI's dependency injection.

    Example:
        with get_db_context() as db:
            obj = crud.model.get(db, id=job_id)

    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def create_all(engine: Engine = engine, sqlmodel_create_all: bool = False) -> None:
    """
    Create all tables in the database.

    Args:
        engine (Engine): database engine.
        sqlmodel_create_all (bool): whether to create all tables using SQLModel.

    Returns:
        None
    """
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line or use
    # sqlmodel_create_all=True
    if sqlmodel_create_all:
        logger.debug("Initializing database...")
        SQLModel.metadata.create_all(bind=engine)
    return


async def initialize_tables_and_initial_data(
    db: Session,
    init_app_specific_data_func: Callable[..., Awaitable[None]] | None = None,
    **kwargs: Any,
) -> None:
    """Initialize database with initial data"""

    # Create all tables
    await create_all(**kwargs)

    # Create superuser
    superuser = await crud.user.get_or_none(db=db, username=settings.FIRST_SUPERUSER_USERNAME)
    if not superuser:
        user_create = models.UserCreateWithPassword(
            username=settings.FIRST_SUPERUSER_USERNAME,
            email=settings.FIRST_SUPERUSER_EMAIL,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
        )
        superuser = await crud.user._create_with_password(db=db, obj_in=user_create)

    # Initialize project specific data
    if init_app_specific_data_func:
        await init_app_specific_data_func(db=db)

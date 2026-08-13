# pylint: disable=E0611,E0401
import logging
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from tortoise.contrib.fastapi import tortoise_exception_handlers

from .config import register_orm, settings
from .logging_config import configure_logging
from .middleware.request_id import RequestIDMiddleware
from .routes import users

configure_logging(settings.ENV)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None]:
    logger.info("Starting Database")
    async with register_orm(app):
        yield
    logger.info("DB connection dropped")


app = FastAPI(
    lifespan=lifespan,
    exception_handlers=tortoise_exception_handlers(),
)

app.add_middleware(RequestIDMiddleware)
app.include_router(users.router)

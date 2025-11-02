# app/main.py
import sentry_sdk
from loguru import logger
import structlog
from app.core.config import settings
import uuid
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware
import logging
from fastapi import FastAPI, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from app.core.database import engine, Base
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.routers import users, shops, orders
from app.crud import order as crud_order
from app.routers import webhooks
from app.logger import logger, RequestIDMiddleware

if settings.SENTRY_DSN:
    sentry_sdk.init(
        dsn=settings.SENTRY_DSN,
        traces_sample_rate=1.0,
        environment=settings.ENVIRONMENT,
    )
structlog.configure(
    processors=[
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.add_log_level,
        structlog.processors.JSONRenderer()
    ]
)
log = structlog.get_logger()
  
# Импорт всех моделей
from app import models

app = FastAPI(title="Coffee Aggregator API")
app.add_middleware(RequestIDMiddleware)

app.include_router(webhooks.router)

app.include_router(users.router)
app.include_router(shops.router)
app.include_router(orders.router)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"request start: {request.method} {request.url}")
    request_id = str(uuid.uuid4())
    request.state.request_id = request_id
    try:
        response = await call_next(request)
        response.headers["X-Request-ID"] = request_id
        logger.info(f"request complete: {request.method} {request.url} -> {response.status_code}")
        return response
    except Exception as e:
        logger.exception("Unhandled exception in request")
        raise


@app.get("/health/db")
async def check_db_connection(db: AsyncSession = Depends(get_db)):
    try:
        result = await db.execute(text("SELECT now()"))
        time = result.scalar_one()
        return {"status": "ok", "time": str(time)}
    except Exception as e:
        return {"status": "error", "details": str(e)}

@app.on_event("startup")
async def startup_event():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    logger.info("Database initialized successfully.")


LOGFILE = "app.log"
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
    handlers=[
        logging.FileHandler(LOGFILE),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("app")

@app.middleware("http")
async def add_request_id(request: Request, call_next):
    request_id = str(uuid.uuid4())
    request.state.request_id = request_id
    logger.bind(request_id=request_id)
    response = await call_next(request)
    response.headers["X-Request-ID"] = request_id
    log.info("request_processed", path=request.url.path, method=request.method, request_id=request_id)
    return response

@app.get("/error")
async def trigger_error():
    division_by_zero = 1 / 0

@app.get("/")
async def root():
    log.info("root_endpoint_called")
    return {"message": "Hello from FastAPI with Sentry + structlog!"}

if settings.SENTRY_DSN:
    app.add_middleware(SentryAsgiMiddleware)
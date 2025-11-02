import logging
from loguru import logger
import sys
import uuid
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

logger.remove()
logger.add(sys.stdout, serialize=True, level="INFO")

class RequestIDMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request_id = str(uuid.uuid4())
        request.state.request_id = request_id

        logger.bind(request_id=request_id).info(f"Request started: {request.url.path}")
        response = await call_next(request)
        response.headers["X-Request-ID"] = request_id
        logger.bind(request_id=request_id).info(f"Request finished: {request.url.path}")
        return response

logger = logging.getLogger("webhook")
logger.setLevel(logging.INFO)

fh = logging.FileHandler("webhook.log")
ch = logging.StreamHandler()

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)

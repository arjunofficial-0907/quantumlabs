import time

from starlette.middleware.base import BaseHTTPMiddleware

from app.core.logger import logger


class RequestLoggerMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request, call_next):

        start_time = time.time()

        response = await call_next(request)

        process_time = time.time() - start_time

        logger.info(
            f"{request.method} {request.url.path} "
            f"Status: {response.status_code} "
            f"Completed in: {process_time:.2f}s"
        )

        return response
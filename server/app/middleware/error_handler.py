from starlette.middleware.base import BaseHTTPMiddleware

from fastapi.responses import JSONResponse

from app.core.logger import logger


class ErrorHandlerMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request, call_next):

        try:

            response = await call_next(request)

            return response

        except Exception as e:

            logger.error(str(e))

            return JSONResponse(
                status_code=500,
                content={
                    "success": False,
                    "message": "Unexpected server error"
                }
            )
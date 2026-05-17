from fastapi import Request
from fastapi.responses import JSONResponse

from sqlalchemy.exc import SQLAlchemyError

from app.core.logger import logger


async def sqlalchemy_exception_handler(
    request: Request,
    exc: SQLAlchemyError
):

    logger.error(str(exc))

    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "message": "Database error occurred"
        }
    )


async def generic_exception_handler(
    request: Request,
    exc: Exception
):

    logger.error(str(exc))

    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "message": "Internal server error"
        }
    )
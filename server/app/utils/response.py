from fastapi.responses import JSONResponse


def success_response(
    message: str,
    data=None,
    status_code: int = 200
):

    return JSONResponse(
        status_code=status_code,
        content={
            "success": True,
            "message": message,
            "data": data
        }
    )


def error_response(
    message: str,
    status_code: int = 400
):

    return JSONResponse(
        status_code=status_code,
        content={
            "success": False,
            "message": message
        }
    )


def paginated_response(
    message: str,
    data,
    total: int,
    page: int,
    limit: int,
    status_code: int = 200
):

    return JSONResponse(
        status_code=status_code,
        content={
            "success": True,
            "message": message,
            "pagination": {
                "total": total,
                "page": page,
                "limit": limit,
                "has_next": total > page * limit
            },
            "data": data
        }
    )
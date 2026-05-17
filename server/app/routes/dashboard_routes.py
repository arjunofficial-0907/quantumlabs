from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.auth.dependencies import (
    admin_required
)

from app.analytics.dashboard_service import (
    get_dashboard_stats
)

from app.utils.response import (
    success_response
)

router = APIRouter(
    prefix="/api/dashboard",
    tags=["Dashboard"]
)


@router.get("/stats")
def dashboard_stats(
    db: Session = Depends(get_db),
    current_user = Depends(admin_required)
):

    stats = get_dashboard_stats(db)

    return success_response(
        "Dashboard stats fetched successfully",
        stats
    )
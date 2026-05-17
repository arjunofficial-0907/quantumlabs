from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Query
from fastapi import status

from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.schemas.service_schema import (
    ServiceCreate,
    ServiceUpdate,
    ServiceResponse
)

from app.services.service_service import (
    create_service_service,
    get_services_service,
    get_service_service,
    update_service_service,
    delete_service_service
)

from app.auth.dependencies import (
    admin_required
)

from app.utils.response import (
    success_response,
    paginated_response
)

from app.models.service_model import Service

router = APIRouter(
    prefix="/api/services",
    tags=["Services"]
)

# ==========================================
# CREATE SERVICE
# ==========================================

@router.post(
    "/",
    response_model=ServiceResponse,
    status_code=status.HTTP_201_CREATED
)
def create_service(
    payload: ServiceCreate,
    db: Session = Depends(get_db),
    current_user = Depends(admin_required)
):

    existing_service = db.query(Service)\
        .filter(Service.slug == payload.slug)\
        .first()

    if existing_service:

        raise HTTPException(
            status_code=400,
            detail="Service slug already exists"
        )

    service = create_service_service(
        db,
        payload
    )

    return service

# ==========================================
# GET ALL SERVICES
# ==========================================

@router.get("/")
def get_services(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    search: str | None = None,
    featured: bool | None = None,
    db: Session = Depends(get_db)
):

    query = db.query(Service)

    # ======================================
    # SEARCH
    # ======================================

    if search:

        query = query.filter(
            Service.title.ilike(f"%{search}%")
        )

    # ======================================
    # FEATURED FILTER
    # ======================================

    if featured is not None:

        query = query.filter(
            Service.featured == featured
        )

    # ======================================
    # TOTAL COUNT
    # ======================================

    total = query.count()

    # ======================================
    # PAGINATION
    # ======================================

    skip = (page - 1) * limit

    services = query\
        .offset(skip)\
        .limit(limit)\
        .all()

    return paginated_response(
        message="Services fetched successfully",
        data=[
            ServiceResponse.model_validate(service).model_dump(mode="json")
            for service in services
        ],
        total=total,
        page=page,
        limit=limit
    )

# ==========================================
# GET FEATURED SERVICES
# ==========================================

@router.get("/featured/list")
def get_featured_services(
    db: Session = Depends(get_db)
):

    services = db.query(Service)\
        .filter(Service.featured == True)\
        .all()

    return success_response(
        "Featured services fetched successfully",
        [
            ServiceResponse.model_validate(service).model_dump(mode="json")
            for service in services
        ]
    )

# ==========================================
# GET SINGLE SERVICE
# ==========================================

@router.get(
    "/{service_id}",
    response_model=ServiceResponse
)
def get_service(
    service_id: str,
    db: Session = Depends(get_db)
):

    service = get_service_service(
        db,
        service_id
    )

    if not service:

        raise HTTPException(
            status_code=404,
            detail="Service not found"
        )

    return service

# ==========================================
# UPDATE SERVICE
# ==========================================

@router.put(
    "/{service_id}",
    response_model=ServiceResponse
)
def update_service(
    service_id: str,
    payload: ServiceUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(admin_required)
):

    service = update_service_service(
        db,
        service_id,
        payload
    )

    if not service:

        raise HTTPException(
            status_code=404,
            detail="Service not found"
        )

    return service

# ==========================================
# DELETE SERVICE
# ==========================================

@router.delete("/{service_id}")
def delete_service(
    service_id: str,
    db: Session = Depends(get_db),
    current_user = Depends(admin_required)
):

    deleted = delete_service_service(
        db,
        service_id
    )

    if not deleted:

        raise HTTPException(
            status_code=404,
            detail="Service not found"
        )

    return success_response(
        "Service deleted successfully"
    )
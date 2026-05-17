from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Request
from fastapi import Query
from fastapi import status

from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.schemas.lead_schema import (
    LeadCreate,
    LeadResponse
)

from app.services.lead_service import (
    create_lead_service,
    get_leads_service,
    get_lead_service,
    delete_lead_service
)

from app.auth.dependencies import (
    admin_required
)

from app.utils.response import (
    success_response,
    paginated_response
)

router = APIRouter(
    prefix="/api/contact",
    tags=["Contact"]
)

# ==========================================
# CREATE CONTACT / LEAD
# ==========================================

@router.post(
    "/",
    response_model=LeadResponse,
    status_code=status.HTTP_201_CREATED
)
def create_contact(
    payload: LeadCreate,
    request: Request,
    db: Session = Depends(get_db)
):

    ip_address = request.client.host

    lead = create_lead_service(
        db=db,
        payload=payload,
        ip_address=ip_address
    )

    return lead

# ==========================================
# GET ALL CONTACTS / LEADS
# ADMIN ONLY
# ==========================================

@router.get("/")
def get_contacts(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    search: str | None = None,
    db: Session = Depends(get_db),
    current_user = Depends(admin_required)
):

    query = get_leads_service(
        db=db,
        skip=0,
        limit=10000
    )

    # ======================================
    # SEARCH FILTER
    # ======================================

    if search:

        filtered = []

        for lead in query:

            if (
                search.lower() in lead.name.lower()
                or search.lower() in lead.email.lower()
            ):
                filtered.append(lead)

        query = filtered

    total = len(query)

    # ======================================
    # PAGINATION
    # ======================================

    start = (page - 1) * limit
    end = start + limit

    paginated_data = query[start:end]

    return paginated_response(
        message="Leads fetched successfully",
        data=[
            LeadResponse.model_validate(
                lead
            ).model_dump(mode="json")
            for lead in paginated_data
        ],
        total=total,
        page=page,
        limit=limit
    )

# ==========================================
# GET SINGLE CONTACT / LEAD
# ADMIN ONLY
# ==========================================

@router.get(
    "/{lead_id}",
    response_model=LeadResponse
)
def get_contact(
    lead_id: str,
    db: Session = Depends(get_db),
    current_user = Depends(admin_required)
):

    lead = get_lead_service(
        db,
        lead_id
    )

    if not lead:

        raise HTTPException(
            status_code=404,
            detail="Lead not found"
        )

    return lead

# ==========================================
# DELETE CONTACT / LEAD
# ADMIN ONLY
# ==========================================

@router.delete("/{lead_id}")
def delete_contact(
    lead_id: str,
    db: Session = Depends(get_db),
    current_user = Depends(admin_required)
):

    deleted = delete_lead_service(
        db,
        lead_id
    )

    if not deleted:

        raise HTTPException(
            status_code=404,
            detail="Lead not found"
        )

    return success_response(
        "Lead deleted successfully"
    )
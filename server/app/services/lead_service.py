from sqlalchemy.orm import Session

from app.models.lead_model import Lead

from app.schemas.lead_schema import LeadCreate


def create_lead_service(
    db: Session,
    payload: LeadCreate,
    ip_address: str = None
):

    lead = Lead(
        **payload.model_dump(),
        ip_address=ip_address
    )

    db.add(lead)

    db.commit()

    db.refresh(lead)

    return lead


def get_leads_service(
    db: Session,
    skip: int = 0,
    limit: int = 10
):

    return db.query(Lead)\
        .offset(skip)\
        .limit(limit)\
        .all()


def get_lead_service(
    db: Session,
    lead_id: str
):

    return db.query(Lead)\
        .filter(Lead.id == lead_id)\
        .first()


def delete_lead_service(
    db: Session,
    lead_id: str
):

    lead = get_lead_service(db, lead_id)

    if not lead:
        return None

    db.delete(lead)

    db.commit()

    return True
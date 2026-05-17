from sqlalchemy.orm import Session

from app.models.service_model import Service

from app.schemas.service_schema import (
    ServiceCreate,
    ServiceUpdate
)


def create_service_service(
    db: Session,
    payload: ServiceCreate
):

    service = Service(**payload.model_dump())

    db.add(service)

    db.commit()

    db.refresh(service)

    return service


def get_services_service(
    db: Session,
    skip: int = 0,
    limit: int = 10
):

    return db.query(Service)\
        .offset(skip)\
        .limit(limit)\
        .all()


def get_service_service(
    db: Session,
    service_id: str
):

    return db.query(Service)\
        .filter(Service.id == service_id)\
        .first()


def update_service_service(
    db: Session,
    service_id: str,
    payload: ServiceUpdate
):

    service = get_service_service(db, service_id)

    if not service:
        return None

    for key, value in payload.model_dump().items():
        setattr(service, key, value)

    db.commit()

    db.refresh(service)

    return service


def delete_service_service(
    db: Session,
    service_id: str
):

    service = get_service_service(db, service_id)

    if not service:
        return None

    db.delete(service)

    db.commit()

    return True
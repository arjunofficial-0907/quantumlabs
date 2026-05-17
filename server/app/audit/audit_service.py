from sqlalchemy.orm import Session

from app.audit.audit_model import AuditLog


def create_audit_log(
    db: Session,
    action: str,
    user_email: str,
    entity: str,
    entity_id: str = None
):

    log = AuditLog(
        action=action,
        user_email=user_email,
        entity=entity,
        entity_id=entity_id
    )

    db.add(log)

    db.commit()

    db.refresh(log)

    return log
from sqlalchemy.orm import Session

from app.models.project_model import Project

from app.schemas.project_schema import (
    ProjectCreate,
    ProjectUpdate
)


# ==========================================
# CREATE PROJECT
# ==========================================

def create_project_service(
    db: Session,
    payload: ProjectCreate
):

    project = Project(**payload.model_dump())

    db.add(project)

    db.commit()

    db.refresh(project)

    return project


# ==========================================
# GET ALL PROJECTS
# ==========================================

def get_projects_service(
    db: Session,
    skip: int = 0,
    limit: int = 10
):

    return db.query(Project)\
        .offset(skip)\
        .limit(limit)\
        .all()


# ==========================================
# GET SINGLE PROJECT
# ==========================================

def get_project_service(
    db: Session,
    project_id: str
):

    return db.query(Project)\
        .filter(Project.id == project_id)\
        .first()


# ==========================================
# UPDATE PROJECT
# ==========================================

def update_project_service(
    db: Session,
    project_id: str,
    payload: ProjectUpdate
):

    project = get_project_service(db, project_id)

    if not project:
        return None

    for key, value in payload.model_dump().items():
        setattr(project, key, value)

    db.commit()

    db.refresh(project)

    return project


# ==========================================
# DELETE PROJECT
# ==========================================

def delete_project_service(
    db: Session,
    project_id: str
):

    project = get_project_service(db, project_id)

    if not project:
        return None

    db.delete(project)

    db.commit()

    return True
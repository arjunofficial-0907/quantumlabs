from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Query
from fastapi import status

from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.schemas.project_schema import (
    ProjectCreate,
    ProjectUpdate,
    ProjectResponse
)

from app.services.project_service import (
    create_project_service,
    get_projects_service,
    get_project_service,
    update_project_service,
    delete_project_service
)

from app.auth.dependencies import (
    admin_required
)

from app.utils.response import (
    success_response,
    paginated_response
)

from app.models.project_model import Project

router = APIRouter(
    prefix="/api/projects",
    tags=["Projects"]
)

# ==========================================
# CREATE PROJECT
# ==========================================

@router.post(
    "/",
    response_model=ProjectResponse,
    status_code=status.HTTP_201_CREATED
)
def create_project(
    payload: ProjectCreate,
    db: Session = Depends(get_db),
    current_user = Depends(admin_required)
):

    existing_project = db.query(Project)\
        .filter(Project.slug == payload.slug)\
        .first()

    if existing_project:

        raise HTTPException(
            status_code=400,
            detail="Project slug already exists"
        )

    project = create_project_service(
        db,
        payload
    )

    return project

# ==========================================
# GET ALL PROJECTS
# ==========================================

@router.get("/")
def get_projects(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    search: str | None = None,
    featured: bool | None = None,
    category: str | None = None,
    db: Session = Depends(get_db)
):

    query = db.query(Project)

    # ======================================
    # SEARCH
    # ======================================

    if search:

        query = query.filter(
            Project.title.ilike(f"%{search}%")
        )

    # ======================================
    # FEATURED FILTER
    # ======================================

    if featured is not None:

        query = query.filter(
            Project.featured == featured
        )

    # ======================================
    # CATEGORY FILTER
    # ======================================

    if category:

        query = query.filter(
            Project.category.ilike(f"%{category}%")
        )

    # ======================================
    # TOTAL COUNT
    # ======================================

    total = query.count()

    # ======================================
    # PAGINATION
    # ======================================

    skip = (page - 1) * limit

    projects = query\
        .offset(skip)\
        .limit(limit)\
        .all()

    return paginated_response(
        message="Projects fetched successfully",
        data=[
            ProjectResponse.model_validate(project).model_dump(mode="json")
            for project in projects
        ],
        total=total,
        page=page,
        limit=limit
    )

# ==========================================
# GET FEATURED PROJECTS
# ==========================================

@router.get("/featured/list")
def get_featured_projects(
    db: Session = Depends(get_db)
):

    projects = db.query(Project)\
        .filter(Project.featured == True)\
        .all()

    return success_response(
        "Featured projects fetched successfully",
        [
            ProjectResponse.model_validate(project).model_dump(mode="json")
            for project in projects
        ]
    )

# ==========================================
# GET SINGLE PROJECT
# ==========================================

@router.get(
    "/{project_id}",
    response_model=ProjectResponse
)
def get_project(
    project_id: str,
    db: Session = Depends(get_db)
):

    project = get_project_service(
        db,
        project_id
    )

    if not project:

        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    return project

# ==========================================
# UPDATE PROJECT
# ==========================================

@router.put(
    "/{project_id}",
    response_model=ProjectResponse
)
def update_project(
    project_id: str,
    payload: ProjectUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(admin_required)
):

    project = update_project_service(
        db,
        project_id,
        payload
    )

    if not project:

        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    return project

# ==========================================
# DELETE PROJECT
# ==========================================

@router.delete("/{project_id}")
def delete_project(
    project_id: str,
    db: Session = Depends(get_db),
    current_user = Depends(admin_required)
):

    deleted = delete_project_service(
        db,
        project_id
    )

    if not deleted:

        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    return success_response(
        "Project deleted successfully"
    )
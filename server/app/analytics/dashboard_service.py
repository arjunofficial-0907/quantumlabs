from sqlalchemy.orm import Session

from app.models.project_model import Project
from app.models.service_model import Service
from app.models.lead_model import Lead
from app.models.user_model import User


def get_dashboard_stats(db: Session):

    total_projects = db.query(Project).count()

    total_services = db.query(Service).count()

    total_leads = db.query(Lead).count()

    total_users = db.query(User).count()

    return {
        "projects": total_projects,
        "services": total_services,
        "leads": total_leads,
        "users": total_users
    }
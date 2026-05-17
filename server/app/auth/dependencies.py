from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import HTTPBearer
from fastapi.security import HTTPAuthorizationCredentials

from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.auth.jwt_handler import verify_access_token

from app.models.user_model import User

security = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):

    token = credentials.credentials

    payload = verify_access_token(token)

    if not payload:

        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )

    user = db.query(User)\
        .filter(User.id == payload["user_id"])\
        .first()

    if not user:

        raise HTTPException(
            status_code=401,
            detail="User not found"
        )

    return user


def admin_required(
    current_user: User = Depends(get_current_user)
):

    if current_user.role != "admin":

        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )

    return current_user
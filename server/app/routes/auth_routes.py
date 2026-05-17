from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.schemas.auth_schema import (
    RegisterSchema,
    LoginSchema
)

from app.services.auth_service import (
    register_user_service,
    login_user_service
)

from app.auth.dependencies import (
    get_current_user
)

from app.models.user_model import User

from app.utils.response import (
    success_response
)

router = APIRouter(
    prefix="/api/auth",
    tags=["Authentication"]
)

# ==========================================
# REGISTER
# ==========================================

@router.post(
    "/register",
    status_code=status.HTTP_201_CREATED
)
def register(
    payload: RegisterSchema,
    db: Session = Depends(get_db)
):

    user = register_user_service(
        db,
        payload
    )

    if not user:

        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    return success_response(
        "User registered successfully",
        {
            "email": user.email,
            "role": user.role
        },
        201
    )

# ==========================================
# LOGIN
# ==========================================

@router.post("/login")
def login(
    payload: LoginSchema,
    db: Session = Depends(get_db)
):

    data = login_user_service(
        db,
        payload
    )

    if not data:

        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    return success_response(
        "Login successful",
        data
    )

# ==========================================
# CURRENT USER
# ==========================================

@router.get("/me")
def get_me(
    current_user: User = Depends(get_current_user)
):

    return success_response(
        "Current user fetched successfully",
        {
            "id": str(current_user.id),
            "name": current_user.name,
            "email": current_user.email,
            "role": current_user.role,
            "is_active": current_user.is_active
        }
    )
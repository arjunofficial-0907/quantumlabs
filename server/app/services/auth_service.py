from sqlalchemy.orm import Session

from app.models.user_model import User

from app.auth.password_handler import (
    hash_password,
    verify_password
)

from app.auth.jwt_handler import (
    create_access_token
)


def register_user_service(
    db: Session,
    payload
):

    existing_user = db.query(User)\
        .filter(User.email == payload.email)\
        .first()

    if existing_user:

        return None

    hashed_password = hash_password(
        payload.password
    )

    user = User(
        name=payload.name,
        email=payload.email,
        password=hashed_password
    )

    db.add(user)

    db.commit()

    db.refresh(user)

    return user


def login_user_service(
    db: Session,
    payload
):

    user = db.query(User)\
        .filter(User.email == payload.email)\
        .first()

    if not user:

        return None

    valid_password = verify_password(
        payload.password,
        user.password
    )

    if not valid_password:

        return None

    token = create_access_token({
        "user_id": str(user.id),
        "email": user.email,
        "role": user.role
    })

    return {
        "token": token,
        "user": {
            "id": str(user.id),
            "name": user.name,
            "email": user.email,
            "role": user.role
        }
    }
from sqlalchemy.orm import Session

from app.tokens.token_model import RefreshToken


def store_refresh_token(
    db: Session,
    user_id: str,
    token: str
):

    refresh_token = RefreshToken(
        user_id=user_id,
        token=token
    )

    db.add(refresh_token)

    db.commit()

    db.refresh(refresh_token)

    return refresh_token


def revoke_refresh_token(
    db: Session,
    token: str
):

    existing_token = db.query(RefreshToken)\
        .filter(RefreshToken.token == token)\
        .first()

    if not existing_token:

        return None

    existing_token.revoked = True

    db.commit()

    return existing_token
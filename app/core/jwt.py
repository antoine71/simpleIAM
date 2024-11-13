import jwt
from config import settings
from datetime import datetime, timedelta, UTC


def encode_access_token(user_id: str):
    exp = datetime.now(UTC) + timedelta(minutes=settings.access_token_lifetime_minutes)
    return jwt.encode(
        {"exp": exp, "sub": user_id},
        key=settings.secret_key,
        algorithm=settings.algorithm,
    )

# here utility functions could be added
from fastapi import APIRouter, Depends, HTTPException, status, Header
from services.auth_service import AuthService
from dependencies import get_auth_service
import jwt
from jwt import ExpiredSignatureError, PyJWTError

# Dependency for verifying JWT token
def verify_token(authorization: str = Header(...), auth_service: AuthService = Depends(get_auth_service)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Bearer token required")

    token = authorization.split()[1]
    try:
        payload = jwt.decode(token, auth_service.secret_key, algorithms=["HS256"])
        return payload
    except ExpiredSignatureError:
        # Token has expired
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token has expired")
    except PyJWTError:
        # Invalid token
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
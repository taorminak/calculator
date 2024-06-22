from fastapi import APIRouter, Depends, HTTPException, status, Header
from services.auth_service import AuthService
from services.user_service import UserService
from services.calculator_service import CalculatorService
from jwt import PyJWTError
import jwt

# Dependency for getting AuthService instance
def get_auth_service() -> AuthService:
    return AuthService()

# Dependency for getting UserService instance
def get_user_service() -> UserService:
    return UserService()

# Dependency for getting CalculatorService instance
def get_calculator_service() -> CalculatorService:
    return CalculatorService()

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


from fastapi import APIRouter, Depends, HTTPException, status
from services.auth_service import AuthService
from dependencies import get_auth_service
from models import User

# Create a router for authentication-related endpoints
router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

# Define login endpoint
@router.post("/login")
def login(user: User, auth_service: AuthService = Depends(get_auth_service)):
    token = auth_service.authenticate_user(user.username, user.password)
    if not token:
        # Raise an exception if authentication fails
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return {"access_token": token}

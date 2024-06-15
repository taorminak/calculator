from fastapi import APIRouter, Depends
from models import CreateUserRequest
from services.user_service import UserService
from dependencies import get_user_service

# Create a router for user-related endpoints
router = APIRouter(
    prefix="/users",
    tags=["users"]
)

# Define endpoint for creating a user
@router.post("/create")
def create_user(user: CreateUserRequest, user_service: UserService = Depends(get_user_service)):
    return user_service.create_user(user)

from services.auth_service import AuthService
from services.user_service import UserService
from services.calculator_service import CalculatorService

# Dependency for getting AuthService instance
def get_auth_service() -> AuthService:
    return AuthService()

# Dependency for getting UserService instance
def get_user_service() -> UserService:
    return UserService()

# Dependency for getting CalculatorService instance
def get_calculator_service() -> CalculatorService:
    return CalculatorService()

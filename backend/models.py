from pydantic import BaseModel
from typing import Optional

# Define a User model with optional role
class User(BaseModel):
    username: str
    password: str
    role: Optional[str] = None

# Define a model for creating a new user request
class CreateUserRequest(BaseModel):
    username: str
    password: str
    role: str

# Define a model for storing calculation details
class Calculation(BaseModel):
    user: str
    operation: str
    operand1: float
    operand2: float
    result: float

# Define a model for operation request with operands
class OperationRequest(BaseModel):
    operand1: float
    operand2: float

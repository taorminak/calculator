from fastapi import APIRouter, Depends, HTTPException, status
from services.calculator_service import CalculatorService
from services.user_service import UserService
from dependencies import get_calculator_service, get_user_service
from utils import verify_token
from models import OperationRequest, User
from constants import ROLE_STUDENT, ROLE_SCIENTIST

# Create a router for calculator-related endpoints
router = APIRouter(prefix="/calculator", tags=["calculator"])


# Every endpoint requires valid token
# Define endpoint for addition
@router.post("/add")
def add(
    request: OperationRequest,
    calculator_service: CalculatorService = Depends(get_calculator_service),
    payload: dict = Depends(verify_token),
    user_service: UserService = Depends(get_user_service),
):
    username = payload.get("sub")
    user_id = user_service.get_user_id(username)
    result = calculator_service.add(user_id, request.operand1, request.operand2)
    return {"result": result}


# Define endpoint for subtraction
@router.post("/subtract")
def subtract(
    request: OperationRequest,
    calculator_service: CalculatorService = Depends(get_calculator_service),
    payload: dict = Depends(verify_token),
    user_service: UserService = Depends(get_user_service),
):
    username = payload.get("sub")
    user_id = user_service.get_user_id(username)
    result = calculator_service.subtract(user_id, request.operand1, request.operand2)
    return {"result": result}


# Define endpoint for multiplication
@router.post("/multiplicate")
def multiplicate(
    request: OperationRequest,
    calculator_service: CalculatorService = Depends(get_calculator_service),
    payload: dict = Depends(verify_token),
    user_service: UserService = Depends(get_user_service),
):
    username = payload.get("sub")
    role = user_service.get_user_role(username)
    user_id = user_service.get_user_id(username)

    if role != ROLE_SCIENTIST:
        raise HTTPException(
            status_code=403, detail="Only scientists have access to this operation."
        )

    result = calculator_service.multiplicate(
        user_id, request.operand1, request.operand2
    )
    return {"result": result}


@router.post("/divide")
def divide(
    request: OperationRequest,
    calculator_service: CalculatorService = Depends(get_calculator_service),
    payload: dict = Depends(verify_token),
    user_service: UserService = Depends(get_user_service),
):
    username = payload.get("sub")
    role = user_service.get_user_role(username)
    user_id = user_service.get_user_id(username)

    if role != ROLE_SCIENTIST:
        raise HTTPException(
            status_code=403, detail=f"Only scientists have access to this operation."
        )
    if request.operand2 == 0:
        raise ValueError("Cannot divide by zero.")
    result = calculator_service.divide(user_id, request.operand1, request.operand2)
    return {"result": result}


@router.post("/modulo")
def modulo(
    request: OperationRequest,
    calculator_service: CalculatorService = Depends(get_calculator_service),
    payload: dict = Depends(verify_token),
    user_service: UserService = Depends(get_user_service),
):
    username = payload.get("sub")
    user_id = user_service.get_user_id(username)
    result = calculator_service.modulo(user_id, request.operand1, request.operand2)
    return {"result": result}


@router.post("/exponentiate")
def exponentiate(
    request: OperationRequest,
    calculator_service: CalculatorService = Depends(get_calculator_service),
    payload: dict = Depends(verify_token),
    user_service: UserService = Depends(get_user_service),
):
    username = payload.get("sub")
    user_id = user_service.get_user_id(username)
    result = calculator_service.exponentiate(
        user_id, request.operand1, request.operand2
    )
    return {"result": result}


@router.get("/history")
def get_all_calculations(
    calculator_service: CalculatorService = Depends(get_calculator_service),
    user_service: UserService = Depends(get_user_service),
    payload: dict = Depends(verify_token),
):
    username = payload.get("sub")
    role = user_service.get_user_role(username)

    if role != ROLE_SCIENTIST:
        raise HTTPException(
            status_code=403, detail="Only scientists have access to this operation."
        )
    return calculator_service.get_calculations()

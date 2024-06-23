from fastapi import APIRouter, Depends, HTTPException, status
from services.calculator_service import CalculatorService
from services.user_service import UserService
from dependencies import get_calculator_service, get_user_service, verify_token
from models import OperationRequest, User

# Create a router for calculator-related endpoints
router = APIRouter(
    prefix="/calculator",
    tags=["calculator"]
)
# Every endpoint requires valid token
# Define endpoint for addition
@router.post("/add")
def add(request: OperationRequest, 
        calculator_service: CalculatorService = Depends(get_calculator_service), 
        token: str = Depends(verify_token)):
    result = calculator_service.add(request.operand1, request.operand2)
    return {"result": result}

# Define endpoint for subtraction
@router.post("/subtract")
def subtract(request: OperationRequest,
            calculator_service: CalculatorService = Depends(get_calculator_service), 
            token: str = Depends(verify_token)):
    result = calculator_service.subtract(request.operand1, request.operand2)
    return {"result": result}

# Define endpoint for multiplication
@router.post("/multiplicate")
def multiplicate(request: OperationRequest, 
                calculator_service: CalculatorService = Depends(get_calculator_service), 
                payload: dict = Depends(verify_token), 
                user_service: UserService = Depends(get_user_service)):
    username = payload.get("username")  
    role = user_service.get_user_role(username)

    if role != "scientist":
        raise HTTPException(status_code=403, detail="Only scientists have access to this operation.")
    
    result = calculator_service.multiplicate(request.operand1, request.operand2)
    return {"result": result}

@router.post("/divide")
def divide(request: OperationRequest, 
            calculator_service: CalculatorService = Depends(get_calculator_service), 
            payload: dict = Depends(verify_token), 
            user_service: UserService = Depends(get_user_service)):
    username = payload.get("sub")  
    role = user_service.get_user_role(username)

    if role != "scientist":
        raise HTTPException(status_code=403, detail=f"Only scientists have access to this operation. Your role is {payload} ")
    
    result = calculator_service.divide(request.operand1, request.operand2)
    return {"result": result}

@router.post("/modulo")
def modulo(request: OperationRequest, 
            calculator_service: CalculatorService = Depends(get_calculator_service), 
            token: str = Depends(verify_token)):
    result = calculator_service.modulo(request.operand1, request.operand2)
    return {"result": result}

@router.post("/exponentiate")
def exponentiate(request: OperationRequest, 
                calculator_service: CalculatorService = Depends(get_calculator_service), 
                token: str = Depends(verify_token)):
    result = calculator_service.exponentiate(request.operand1, request.operand2)
    return {"result": result}

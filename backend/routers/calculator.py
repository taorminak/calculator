from fastapi import APIRouter, Depends, HTTPException, status
from services.calculator_service import CalculatorService
from dependencies import get_calculator_service, verify_token
from models import OperationRequest

# Create a router for calculator-related endpoints
router = APIRouter(
    prefix="/calculator",
    tags=["calculator"]
)
# Every endpoint requires valid token
# Define endpoint for addition
@router.post("/add")
def add(request: OperationRequest, calculator_service: CalculatorService = Depends(get_calculator_service), token: str = Depends(verify_token)):
    result = calculator_service.add(request.operand1, request.operand2)
    return {"result": result}

# Define endpoint for subtraction
@router.post("/subtract")
def subtract(request: OperationRequest, calculator_service: CalculatorService = Depends(get_calculator_service), token: str = Depends(verify_token)):
    result = calculator_service.subtract(request.operand1, request.operand2)
    return {"result": result}

# Define endpoint for addition
@router.post("/multiplicate")
def multiplicate(request: OperationRequest, calculator_service: CalculatorService = Depends(get_calculator_service), token: str = Depends(verify_token)):
    result = calculator_service.multiplicate(request.operand1, request.operand2)
    return {"result": result}

@router.post("/divide")
def divide(request: OperationRequest, calculator_service: CalculatorService = Depends(get_calculator_service), token: str = Depends(verify_token)):
    result = calculator_service.divide(request.operand1, request.operand2)
    return {"result": result}

@router.post("/modulo")
def modulo(request: OperationRequest, calculator_service: CalculatorService = Depends(get_calculator_service), token: str = Depends(verify_token)):
    result = calculator_service.modulo(request.operand1, request.operand2)
    return {"result": result}

@router.post("/exponentiate")
def exponentiate(request: OperationRequest, calculator_service: CalculatorService = Depends(get_calculator_service), token: str = Depends(verify_token)):
    result = calculator_service.exponentiate(request.operand1, request.operand2)
    return {"result": result}

from fastapi import APIRouter, Depends, HTTPException, status
from services.calculator_service import CalculatorService
from dependencies import get_calculator_service
from models import OperationRequest

# Create a router for calculator-related endpoints
router = APIRouter(
    prefix="/calculator",
    tags=["calculator"]
)

# Define endpoint for addition
@router.post("/add")
def add(request: OperationRequest, calculator_service: CalculatorService = Depends(get_calculator_service)):
    result = calculator_service.add(request.operand1, request.operand2)
    return {"result": result}

# Define endpoint for subtraction
@router.post("/subtract")
def subtract(request: OperationRequest, calculator_service: CalculatorService = Depends(get_calculator_service)):
    result = calculator_service.subtract(request.operand1, request.operand2)
    return {"result": result}

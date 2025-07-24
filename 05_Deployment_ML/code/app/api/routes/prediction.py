from fastapi import APIRouter, Depends, HTTPException
from app.models.schemas import CreditCardInput, PredictionResponse, ModelInfo
from app.services.prediction_service import PredictionService
from app.api.dependencies import get_prediction_service

router = APIRouter(prefix="/api/v1", tags=["prediction"])

@router.post("/predict", response_model=PredictionResponse)
async def predict_default(
    data: CreditCardInput,
    service: PredictionService = Depends(get_prediction_service)
):
    try:
        return service.predict(data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/model/info", response_model=ModelInfo)
async def get_model_info():
    return ModelInfo(
        name="Credit Card Default Predictor",
        version="1.0.0",
        accuracy=0.85,
        features=["LIMIT_BAL", "SEX", "EDUCATION", "MARRIAGE", "AGE", "PAY_0", "PAY_2", "PAY_3", "PAY_4", "PAY_5", "PAY_6", "BILL_AMT1", "BILL_AMT2", "BILL_AMT3", "BILL_AMT4", "BILL_AMT5", "BILL_AMT6", "PAY_AMT1", "PAY_AMT2", "PAY_AMT3", "PAY_AMT4", "PAY_AMT5", "PAY_AMT6"]
    )

@router.get("/health")
async def health_check():
    return {"status": "healthy", "message": "API is running"}
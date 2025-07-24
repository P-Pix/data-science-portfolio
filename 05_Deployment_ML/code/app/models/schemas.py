from pydantic import BaseModel, Field, validator
from typing import Optional, List
from enum import IntEnum

class SexEnum(IntEnum):
    MALE = 1
    FEMALE = 2

class EducationEnum(IntEnum):
    GRADUATE = 1
    UNIVERSITY = 2
    HIGH_SCHOOL = 3
    OTHERS = 4

class CreditCardInput(BaseModel):
    LIMIT_BAL: int = Field(..., ge=1, description="Limite de crédit")
    SEX: SexEnum = Field(..., description="Sexe (1=Male, 2=Female)")
    EDUCATION: EducationEnum = Field(..., description="Niveau d'éducation")
    MARRIAGE: int = Field(..., ge=1, le=3, description="Statut marital")
    AGE: int = Field(..., ge=18, le=100, description="Âge")
    PAY_0: int = Field(..., ge=-2, le=8, description="Statut de paiement")
    # ... autres champs avec validation
    
    @validator('LIMIT_BAL')
    def validate_limit(cls, v):
        if v <= 0:
            raise ValueError('La limite doit être positive')
        return v

class PredictionResponse(BaseModel):
    prediction: int
    probability: float
    confidence: str
    interpretation: str

class ModelInfo(BaseModel):
    name: str
    version: str
    accuracy: float
    features: List[str]
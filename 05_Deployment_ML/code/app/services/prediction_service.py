import joblib
import numpy as np
from typing import Dict, Any
from app.models.schemas import CreditCardInput, PredictionResponse
from app.config import settings

class PredictionService:
    def __init__(self):
        self.model = None
        self.load_model()
    
    def load_model(self):
        try:
            self.model = joblib.load(f"{settings.model_path}credit_card_default_model.pkl")
        except Exception as e:
            raise Exception(f"Erreur lors du chargement du modèle: {e}")
    
    def predict(self, data: CreditCardInput) -> PredictionResponse:
        try:
            # Préparation des données
            features = self._prepare_features(data)
            
            # Prédiction
            prediction = self.model.predict([features])[0]
            probability = self.model.predict_proba([features])[0].max()
            
            # Interprétation
            interpretation = self._interpret_prediction(prediction, probability)
            confidence = self._get_confidence_level(probability)
            
            return PredictionResponse(
                prediction=int(prediction),
                probability=float(probability),
                confidence=confidence,
                interpretation=interpretation
            )
        except Exception as e:
            raise Exception(f"Erreur lors de la prédiction: {e}")
    
    def _prepare_features(self, data: CreditCardInput) -> np.ndarray:
        return np.array([
            data.LIMIT_BAL, data.SEX, data.EDUCATION, data.MARRIAGE, data.AGE,
            data.PAY_0, data.PAY_2, data.PAY_3, data.PAY_4, data.PAY_5, data.PAY_6,
            data.BILL_AMT1, data.BILL_AMT2, data.BILL_AMT3, data.BILL_AMT4, data.BILL_AMT5, data.BILL_AMT6,
            data.PAY_AMT1, data.PAY_AMT2, data.PAY_AMT3, data.PAY_AMT4, data.PAY_AMT5, data.PAY_AMT6
        ])
    
    def _interpret_prediction(self, prediction: int, probability: float) -> str:
        if prediction == 1:
            return f"Risque élevé de défaut de paiement (probabilité: {probability:.2%})"
        else:
            return f"Faible risque de défaut de paiement (probabilité: {(1-probability):.2%})"
    
    def _get_confidence_level(self, probability: float) -> str:
        if probability > 0.8:
            return "Très élevée"
        elif probability > 0.6:
            return "Élevée"
        elif probability > 0.4:
            return "Moyenne"
        else:
            return "Faible"
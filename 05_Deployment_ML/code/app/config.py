from pydantic import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    app_name: str = "ML Prediction API"
    debug: bool = False
    model_path: str = "models/"
    cors_origins: list = ["*"]
    
    class Config:
        env_file = ".env"

settings = Settings()
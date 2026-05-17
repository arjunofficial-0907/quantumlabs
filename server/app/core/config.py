from pydantic_settings import BaseSettings
from pydantic import ConfigDict


class Settings(BaseSettings):

    APP_NAME: str = "Quantum Labs API"

    APP_VERSION: str = "1.0.0"

    PORT: int = 8000

    DATABASE_URL: str

    JWT_SECRET: str

    FRONTEND_URL: str = "http://localhost:5173"

    model_config = ConfigDict(
        env_file=".env",
        extra="ignore"
    )

    CLOUDINARY_CLOUD_NAME: str

    CLOUDINARY_API_KEY: str

    CLOUDINARY_API_SECRET: str


settings = Settings()
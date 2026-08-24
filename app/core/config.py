from pydantic_settings import  BaseSettings

class Settings(BaseSettings):
    DATABASE_URL:str
    APP_NAME: str = "My FastAPI App"
    DEBUG: bool = True
    ENVIRONMENT: str = "development"
    class Config:
        env_file=".env"
        env_file_encoding="utf-8"

settings=Settings()
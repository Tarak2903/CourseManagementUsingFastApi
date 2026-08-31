from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL:str="postgresql://postgres:Tarak%4029@localhost:5432/CourseManagementDatabase"
    APP_NAME: str = "My FastAPI App"
    DEBUG: bool = True
    ENVIRONMENT: str = "development"
    SECRET_KEY:str
    ALGORITHM:str
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )
settings=Settings()
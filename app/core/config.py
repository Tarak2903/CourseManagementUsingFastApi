from pydantic_settings import  BaseSettings

class Settings(BaseSettings):
    DATABASE_URL:str="postgresql://postgres:Tarak%4029@localhost:5432/CourseManagementDatabase"
    APP_NAME: str = "My FastAPI App"
    DEBUG: bool = True
    ENVIRONMENT: str = "development"

settings=Settings()
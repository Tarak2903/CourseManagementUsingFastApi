from pydantic import BaseModel,Field
from app.core.enums import Role
class UserCreate(BaseModel):
    name:str=Field(min_length=1,max_length=20)
    user_name:str=Field(min_length=1,max_length=20)
    password:str=Field(min_length=7,max_length=20)
    role:Role

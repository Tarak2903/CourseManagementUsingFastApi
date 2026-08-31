from pydantic import Field, BaseModel


class UserLogin(BaseModel):
    user_name:str=Field(min_length=1,max_length=20)
    password:str=Field(min_length=7,max_length=20)
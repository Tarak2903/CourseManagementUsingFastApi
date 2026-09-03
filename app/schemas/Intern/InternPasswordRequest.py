from pydantic import BaseModel, Field


class InternPasswordRequest(BaseModel):
    password:str=Field(min_length=7,max_length=20)
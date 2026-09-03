from pydantic import BaseModel


class InternResponse(BaseModel):
    intern_name:str
    intern_user_name:str
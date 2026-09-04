from pydantic import BaseModel


class PasswordChangeResponse(BaseModel):
    updated: bool

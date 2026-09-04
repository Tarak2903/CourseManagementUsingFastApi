from pydantic import BaseModel

from app.schemas.Intern.InternResponse import InternResponse


class InternListResponse(BaseModel):
    interns: list[InternResponse]

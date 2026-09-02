from pydantic import BaseModel, Field


class EnrollmentRequest(BaseModel):
    interns:list[int]=Field(min_length=1)
    course_code:int=Field(gt=0)

from pydantic import BaseModel


class EnrollmentResponse(BaseModel):
    course_code: int
    interns: list[int]

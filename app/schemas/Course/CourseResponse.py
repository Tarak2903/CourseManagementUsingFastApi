from pydantic import BaseModel


class CourseResponse(BaseModel):
    course_name: str
    total_sections: int
    course_code: int

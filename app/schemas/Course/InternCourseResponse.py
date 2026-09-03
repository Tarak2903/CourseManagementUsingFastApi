from pydantic import BaseModel


class InternCourseResponse(BaseModel):
    course_name:str
    total_sections:int
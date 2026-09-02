from pydantic import BaseModel, Field


class CourseCreationRequest(BaseModel):
    name:str=Field(max_length=20,min_length=1)
    total_section:int=Field(gt=0)
    course_code:int=Field(gt=0)

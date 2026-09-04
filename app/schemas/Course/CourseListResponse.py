from pydantic import BaseModel

from app.schemas.Course.CourseResponse import CourseResponse


class CourseListResponse(BaseModel):
    courses: list[CourseResponse]

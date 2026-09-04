from pydantic import BaseModel

from app.schemas.Course.InternCourseProgressResponse import InternProgressResponse


class InternProgressListResponse(BaseModel):
    progress: list[InternProgressResponse]

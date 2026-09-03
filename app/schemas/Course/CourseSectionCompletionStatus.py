from pydantic import BaseModel


class CourseSectionCompletionStatus(BaseModel):
    section:int
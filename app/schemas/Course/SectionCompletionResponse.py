from pydantic import BaseModel


class SectionCompletionResponse(BaseModel):
    sections_completed_in_this_operation: int

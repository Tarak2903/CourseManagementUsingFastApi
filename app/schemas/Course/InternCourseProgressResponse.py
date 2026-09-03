from pydantic import BaseModel, Field, PositiveFloat


class InternProgressResponse(BaseModel):
    course_name:str
    total_sections:int
    sections_completed:int
    percentage_completed:float




# {
#     status:
#     data: {
#
#           }
#   message:
#   error
# }
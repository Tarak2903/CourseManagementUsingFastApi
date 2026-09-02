from app.exceptions.ResourceNotFoundException import ResourceNotFoundException


class CourseNotFoundException(ResourceNotFoundException):
    def __init__(self,message):
        self.message=message
        super().__init__(message)
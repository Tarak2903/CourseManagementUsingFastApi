from sqlalchemy.orm import Session

from app.models.enrollment import Enrollment


class EnrollmentRepository:
    def __init__(self,db:Session):
        self.db=db


    def enroll_intern(self,ls_interns,course_id):
        ls_enrollment=[]

        for intern_id in ls_interns:
            enrollment_model=Enrollment(intern_id=intern_id,course_id=course_id,section_completed=0)
            ls_enrollment.append(enrollment_model)

        self.db.add_all(ls_enrollment)
        self.db.commit()


from sqlalchemy.orm import Session

from app.models.course import Course
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


    def get_intern_progress(self,intern_id):
        return (
            self.db.query(Enrollment, Course)
            .join(Course, Enrollment.course_id == Course.id)
            .filter(Enrollment.intern_id == intern_id)
            .all()
        )

    def get_interns_courses(self,intern_id):
        return (
            self.db.query(Enrollment,Course).filter(Enrollment.intern_id==intern_id,Enrollment.course_id==Course.id).all()
        )

    def get_intern_course_info(self,course_id,intern_id):
        return (
            self.db.query(Enrollment,Course).
            filter(Enrollment.intern_id==intern_id,Enrollment.course_id==course_id,
            Enrollment.course_id==Course.id).first()
        )

    def section_request_validation(self,course_id,intern_id):
        return (self.db.query(Enrollment.section_completed,Course.total_section).
         filter(Enrollment.intern_id==intern_id,Enrollment.course_id==course_id,Enrollment.course_id==Course.id)).first()

    def complete_section(self,course_id,intern_id,section):
        enrollment=self.db.query(Enrollment).filter(Enrollment.course_id==course_id,Enrollment.intern_id==intern_id).first()
        enrollment.section_completed+=section
        self.db.commit()
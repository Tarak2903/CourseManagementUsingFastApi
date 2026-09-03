from fastapi import FastAPI
from app.models import enrollment
from app.models import user
from app.models import course
from app.core.database import Base,engine
from app.exceptions.ResourceNotFoundException import ResourceNotFoundException
from app.exceptions.ResrouceAlreadyExistsException import ResourceAlreadyExistsException
from app.exceptions.UnauthenticatedException import  UnauthenticatedException
from app.exceptions.ForbiddenException import ForbiddenException
from app.exceptions.handler import resource_already_exists_exception, resource_doesnt_exists_exception, \
    unauthenticated_exception, forbidden_exception

Base.metadata.create_all(bind=engine)
from app.api.v1.endpoints.intern import router as user_router
from app.api.v1.endpoints.mentor import router as mentor_router
from app.api.v1.endpoints.auth import router as auth_router
from app.api.v1.endpoints.course import router as course_router
from app.api.v1.endpoints.enrollment import router as enrollment_router
app=FastAPI()
app.include_router(user_router)
app.include_router(mentor_router)
app.include_router(auth_router)
app.include_router(course_router)
app.include_router(enrollment_router)

app.add_exception_handler(
    ResourceAlreadyExistsException,
    resource_already_exists_exception
)
app.add_exception_handler(
    ResourceNotFoundException,
    resource_doesnt_exists_exception
)
app.add_exception_handler(
    UnauthenticatedException,
    unauthenticated_exception
)
app.add_exception_handler(
    ForbiddenException,
    forbidden_exception
)

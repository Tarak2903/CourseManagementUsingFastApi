from fastapi import FastAPI
from app.core.database import Base,engine
from app.exceptions.ResourceNotFoundException import ResourceNotFoundException
from app.exceptions.ResrouceAlreadyExistsException import ResourceAlreadyExistsException
from app.exceptions.UnAuthorizedException import UnAuthorizedException
from app.exceptions.handler import resource_already_exists_exception, resource_doesnt_exists_exception, \
    unauthorized_exception

Base.metadata.create_all(bind=engine)
from app.api.v1.endpoints.user import router as user_router
from app.api.v1.endpoints.mentor import router as mentor_router
from app.api.v1.endpoints.auth import router as auth_router


app=FastAPI()
app.include_router(user_router)
app.include_router(mentor_router)
app.include_router(auth_router)

app.add_exception_handler(
    ResourceAlreadyExistsException,
    resource_already_exists_exception
)
app.add_exception_handler(
    ResourceNotFoundException,
    resource_doesnt_exists_exception
)
app.add_exception_handler(
    UnAuthorizedException,
    unauthorized_exception
)

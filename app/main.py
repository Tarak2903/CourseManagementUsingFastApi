from fastapi import FastAPI
from app.core.database import Base,engine
from app.exceptions.ResrouceAlreadyExistsException import ResourceAlreadyExistsException
from app.exceptions.handler import resource_already_exists_exception
Base.metadata.create_all(bind=engine)
from app.api.v1.endpoints.user import router as user_router

app=FastAPI()

app.include_router(user_router)
app.add_exception_handler(
    ResourceAlreadyExistsException,
    resource_already_exists_exception
)

from fastapi import Request
from fastapi.responses import JSONResponse

from app.exceptions.ResrouceAlreadyExistsException import ResourceAlreadyExistsException


async def resource_already_exists_exception(request:Request,exc:ResourceAlreadyExistsException):
    return JSONResponse(
        status_code=409,
        content={
            "detail":exc.message
        }
    )
from fastapi import Request
from fastapi.responses import JSONResponse

from app.exceptions.UnauthenticatedException import UnauthenticatedException
from app.exceptions.ResourceNotFoundException import ResourceNotFoundException
from app.exceptions.ResrouceAlreadyExistsException import ResourceAlreadyExistsException
from app.exceptions.ForbiddenException import  ForbiddenException


async def resource_already_exists_exception(request:Request,exc:ResourceAlreadyExistsException):
    return JSONResponse(
        status_code=409,
        content={
            "detail":exc.message
        }
    )
async def resource_doesnt_exists_exception(request:Request,exc:ResourceNotFoundException):
    return JSONResponse(
        status_code=404,
        content={
            "detail":exc.message
        }
    )

async def unauthenticated_exception(request:Request,exc:UnauthenticatedException):
    return JSONResponse(
        status_code=401,
        content={
            "detail":exc.message
        }

    )
async def forbidden_exception(request:Request,exc:ForbiddenException):
    return JSONResponse(
        status_code=403,
        content={
            "detail":exc.message
        }
    )
from fastapi import HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.exceptions.InvalidOperationException import InvalidOperationException
from app.exceptions.UnauthenticatedException import UnauthenticatedException
from app.exceptions.ResourceNotFoundException import ResourceNotFoundException
from app.exceptions.ResrouceAlreadyExistsException import ResourceAlreadyExistsException
from app.exceptions.ForbiddenException import ForbiddenException
from app.schemas.APIResponse import APIResponse, ErrorDetail


def _error_response(status_code: int, message: str, details: list[ErrorDetail] | None = None,
                    headers: dict[str, str] | None = None):
    return JSONResponse(
        status_code=status_code,
        content=APIResponse(
            success=False,
            message=message,
            data={},
            errors=details or [ErrorDetail(code=status_code, details=message)]
        ).model_dump(mode="json"),
        headers=headers
    )


async def resource_already_exists_exception(request: Request, exc: ResourceAlreadyExistsException):
    return _error_response(409, exc.message)


async def resource_doesnt_exists_exception(request: Request, exc: ResourceNotFoundException):
    return _error_response(404, exc.message)


async def unauthenticated_exception(request: Request, exc: UnauthenticatedException):
    return _error_response(401, exc.message)


async def forbidden_exception(request: Request, exc: ForbiddenException):
    return _error_response(403, exc.message)


async def invalid_operation_exception(request: Request, exc: InvalidOperationException):
    return _error_response(400, exc.message)


async def http_exception(request: Request, exc: HTTPException):
    message = exc.detail if isinstance(exc.detail, str) else str(exc.detail)
    return _error_response(
        exc.status_code,
        message,
        headers=exc.headers
    )


async def validation_exception(request: Request, exc: RequestValidationError):
    details = [
        ErrorDetail(
            code=422,
            details=f"{'.'.join(str(location) for location in error['loc'])}: {error['msg']}"
        )
        for error in exc.errors()
    ]

    return _error_response(422, "Validation error", details=details)

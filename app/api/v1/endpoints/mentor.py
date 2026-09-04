from fastapi import APIRouter, Depends

from app.core.dependency import get_intern_service
from app.core.security import get_current_mentor
from app.models.user import User
from app.schemas.APIResponse import APIResponse
from app.schemas.Intern.InternCreationRequest import InternCreationRequest
from app.schemas.Intern.InternResponse import InternResponse
from app.services.InternService import InternService

router = APIRouter()


@router.post('/interns', response_model=APIResponse[InternResponse], tags=['Mentor'])
async def add_intern(intern: InternCreationRequest,
                     intern_service: InternService = Depends(get_intern_service),
                     mentor: User = Depends(get_current_mentor)):
    created_intern = intern_service.add_intern(intern, mentor.id)

    return APIResponse(
        success=True,
        message="Intern registered successfully",
        data=InternResponse(
            intern_name=created_intern.name,
            intern_user_name=created_intern.user_name
        )
    )

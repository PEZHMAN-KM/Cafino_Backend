from fastapi import APIRouter
from dependencies.dependencies import DB_DEPENDENCY
from dependencies.body_dependencies import NAME_BODY
from dependencies.access_dependencies import USER_DEPENDENCY
from schemas.user_schemas import UserDisplay, UserModel
from functions import user_functions


router = APIRouter(
    prefix='/admin_user',
    tags=['Admin User']
)


@router.post('/create_user', status_code=201, response_model=UserDisplay)
async def create_user(request: UserModel, db: DB_DEPENDENCY):
    return await user_functions.create_user(request=request, db=db)

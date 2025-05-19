from fastapi import APIRouter
from functions import user_functions
from dependencies.dependencies import DB_DEPENDENCY
from dependencies.body_dependencies import NAME_BODY
from dependencies.access_dependencies import USER_DEPENDENCY
from schemas.user_schemas import UserDisplay, UserModel, UpdateUserModel


router = APIRouter(
    prefix='/user',
    tags=['User']
)


@router.put('/update_self_info', status_code=200, response_model=UserDisplay)
async def update_self_info(request: UpdateUserModel, user: USER_DEPENDENCY, db: DB_DEPENDENCY):
    return await user_functions.update_self_user(request=request, user_id=user.id, db=db)


@router.put('/self_unemplyment', status_code=200, response_model=UserDisplay)
async def self_unemplyment(user: USER_DEPENDENCY, db: DB_DEPENDENCY):
    return await user_functions.self_unemplyment(user_id=user.id, db=db)


@router.get('/get_self_info', status_code=200, response_model=UserDisplay)
async def get_self_info(user: USER_DEPENDENCY, db: DB_DEPENDENCY):
    return await user_functions.get_self_info(user_id=user.id, db=db)
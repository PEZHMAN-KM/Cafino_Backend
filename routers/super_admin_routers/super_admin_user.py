from fastapi import APIRouter
from schemas.user_schemas import UserDisplay, UserModel, AdminUpdateModel
from functions import user_functions
from dependencies.dependencies import DB_DEPENDENCY
from dependencies.body_dependencies import ID_BODY
from dependencies.access_dependencies import ROUTER_SUPER_ADMIN_DEPENDENCY


router = APIRouter(
    prefix='/super_admin/user',
    tags=['Super Admin User'],
    dependencies=[ROUTER_SUPER_ADMIN_DEPENDENCY]
)


@router.post('/update_user_super_admin', status_code=201, response_model=UserDisplay)
async def update_user_super_admin(request: AdminUpdateModel, db: DB_DEPENDENCY):
    return await user_functions.update_user_super_admin(request=request, db=db)


@router.delete('/delete_user', status_code=200)
async def delete_user(user_id: ID_BODY, db: DB_DEPENDENCY):
    return await user_functions.delete_user(user_id=user_id, db=db)


@router.get('/get_all_users', status_code=200, response_model=list[UserDisplay])
async def get_all_users(db: DB_DEPENDENCY):
    return await user_functions.get_all_users(db=db)


@router.get('/get_user', status_code=200, response_model=UserDisplay)
async def get_user(user_id: ID_BODY, db: DB_DEPENDENCY):
    return await user_functions.get_user(user_id=user_id, db=db)
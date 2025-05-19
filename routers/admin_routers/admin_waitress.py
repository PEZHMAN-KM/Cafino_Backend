from fastapi import APIRouter
from schemas.user_schemas import UserDisplay, UserModel, AdminUpdateModel
from functions import user_functions
from dependencies.dependencies import DB_DEPENDENCY
from dependencies.body_dependencies import ID_BODY
from dependencies.access_dependencies import ROUTER_ADMIN_DEPENDENCY


router = APIRouter(
    prefix='/admin/waitress',
    tags=['Admin Waitress'],
    dependencies=[ROUTER_ADMIN_DEPENDENCY]
)


@router.post('/create_waitress', status_code=201, response_model=UserDisplay)
async def create_waitress(request: UserModel, db: DB_DEPENDENCY):
    return await user_functions.create_waitress(request=request, db=db)


@router.put('/update_waitress', status_code=200, response_model=UserDisplay)
async def update_by_admin(request: AdminUpdateModel, db: DB_DEPENDENCY):
    return await user_functions.update_by_admin(request=request, db=db)


@router.put('/admin_unemploy_user', status_code=200, response_model=UserDisplay)
async def admin_unemploy_user(user_id: ID_BODY, db: DB_DEPENDENCY):
    return await user_functions.admin_unemploy_user(user_id=user_id, db=db)


@router.get('/get_all_waitresses', status_code=200, response_model=list[UserDisplay])
async def get_all_waitresses(db: DB_DEPENDENCY):
    return await user_functions.get_all_waitresses(db=db)
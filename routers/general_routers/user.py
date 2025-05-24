from fastapi import APIRouter, UploadFile
from functions import user_functions
from dependencies.dependencies import DB_DEPENDENCY
from dependencies.body_dependencies import ID_BODY
from dependencies.access_dependencies import USER_DEPENDENCY
from schemas.user_schemas import UserDisplay, UserModel, UpdateUserModel
from fastapi.responses import FileResponse



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


@router.put('/update_user_pic', status_code=200, response_model=UserDisplay)
async def update_user_pic(pic: UploadFile, user: USER_DEPENDENCY, db: DB_DEPENDENCY):
    return await user_functions.update_user_pic(user_id=user.id, pic=pic, db=db)


@router.put('/delete_user_pic', status_code=200, response_model=UserDisplay)
async def delete_user_pic(user: USER_DEPENDENCY, db: DB_DEPENDENCY):
    return await user_functions.delete_user_pic(user_id=user.id, db=db)


@router.post('get_user_picture', status_code=200, response_class=FileResponse)
async def get_user_pic(user_id: ID_BODY, db: DB_DEPENDENCY):
    return await user_functions.get_user_pic(user_id=user_id, db=db)

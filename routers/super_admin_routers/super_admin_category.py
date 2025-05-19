from fastapi import APIRouter
from schemas.category_schema import UpdateCategoryModel, CategoryDisplay
from functions import category_functions
from dependencies.dependencies import DB_DEPENDENCY
from dependencies.body_dependencies import ID_BODY, NAME_BODY
from dependencies.access_dependencies import ROUTER_SUPER_ADMIN_DEPENDENCY


router = APIRouter(
    prefix='/super_admin/category',
    tags=['Super Admin Category'],
    dependencies=[ROUTER_SUPER_ADMIN_DEPENDENCY]
)


@router.post('/add_category', status_code=201, response_model=CategoryDisplay)
async def add_category(name: NAME_BODY, db: DB_DEPENDENCY):
    return await category_functions.add_category(name=name, db=db)


@router.put('/update_category', status_code=200, response_model=CategoryDisplay)
async def update_category(info: UpdateCategoryModel, db: DB_DEPENDENCY):
    return await category_functions.update_category(info=info, db=db)


@router.delete('/delete_category', status_code=200, response_model=str)
async def delete_category(category_id: ID_BODY, db: DB_DEPENDENCY):
    return await category_functions.delete_category(category_id=category_id, db=db)







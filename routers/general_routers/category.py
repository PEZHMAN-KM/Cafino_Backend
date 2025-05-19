from fastapi import APIRouter
from functions import category_functions
from dependencies.dependencies import DB_DEPENDENCY
from dependencies.body_dependencies import ID_BODY
from dependencies.access_dependencies import USER_DEPENDENCY
from schemas.category_schema import CategoryDisplay


router = APIRouter(
    prefix='/category',
    tags=['Category']
)


@router.get('/get_all_categories', status_code=200, response_model=list[CategoryDisplay])
async def get_all_categories(db: DB_DEPENDENCY):
    return await category_functions.get_all_categories(db=db)


@router.post('/get_category', status_code=200, response_model=CategoryDisplay)
async def get_category(category_id: ID_BODY, db: DB_DEPENDENCY):
    return await category_functions.get_category(category_id=category_id, db=db)
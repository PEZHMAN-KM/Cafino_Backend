from fastapi import APIRouter
from functions import food_functions
from dependencies.dependencies import DB_DEPENDENCY
from dependencies.body_dependencies import ID_BODY
from fastapi.responses import FileResponse
from schemas.food_schemas import FoodDisplay, ShowFoodsOfCategory


router = APIRouter(
    prefix='/food',
    tags=['Food']
)


@router.post('/get_food', status_code=200, response_model=FoodDisplay)
async def get_food(food_id: ID_BODY, db: DB_DEPENDENCY):
    return await food_functions.get_food(food_id=food_id, db=db)


@router.get('/get_all_foods', status_code=200, response_model=list[FoodDisplay])
async def get_all_foods(db: DB_DEPENDENCY):
    return await food_functions.get_all_foods(db=db)


@router.post('/get_foods_of_category', status_code=200, response_model=list[FoodDisplay])
async def get_foods_of_category(category_id: ID_BODY, db: DB_DEPENDENCY):
    return await food_functions.get_foods_of_category(category_id=category_id, db=db)


@router.get('/get_all_on_sale_foods', status_code=200, response_model=list[FoodDisplay])
async def get_all_on_sale_foods(db: DB_DEPENDENCY):
    return await food_functions.get_all_on_sale_foods(db=db)


@router.post('/show_category_foods', status_code=200, response_model=ShowFoodsOfCategory)
async def show_category_foods(category_id: ID_BODY, db: DB_DEPENDENCY):
    return await food_functions.show_category_foods(category_id=category_id, db=db)


@router.post('/search_food', status_code=200, response_model=list[FoodDisplay])
async def search_food(search: str, db: DB_DEPENDENCY):
    return await food_functions.search_food(search=search, db=db)


@router.post('/get_food_list_by_id', status_code=200, response_model=list[FoodDisplay])
async def get_food_list_by_id(id_list: list[int], db: DB_DEPENDENCY):
    return await food_functions.get_food_list_by_id(id_list=id_list, db=db)


@router.post('/get_food_picture', status_code=200, response_class=FileResponse)
async def get_food_pic(food_id: ID_BODY, db: DB_DEPENDENCY):
    return await food_functions.get_food_pic(food_id=food_id, db=db)

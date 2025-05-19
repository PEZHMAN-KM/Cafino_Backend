from fastapi import APIRouter, UploadFile, Form
from schemas.food_schemas import FoodDisplay, AddFoodModel, UpdateFoodModel, CategoryOnSale
from functions import food_functions
from dependencies.dependencies import DB_DEPENDENCY
from dependencies.body_dependencies import ID_BODY
from dependencies.access_dependencies import ROUTER_ADMIN_DEPENDENCY, ADMIN_DEPENDENCY

router = APIRouter(
    prefix='/admin/food',
    tags=['Admin Food'],
    dependencies=[ROUTER_ADMIN_DEPENDENCY]
)


@router.post('/add_food', status_code=201, response_model=FoodDisplay)
async def add_food(db: DB_DEPENDENCY,
                   name: str = Form(...),
                   price: int = Form(...),
                   description: str = Form(None),
                   category_id: int = Form(...),
                   in_sale: bool = Form(None),
                   sale_price: int = Form(None),
                   pic: UploadFile | None = None):
    request = AddFoodModel(
        name=name,
        price=price,
        description=description,
        category_id=category_id,
        in_sale=in_sale,
        sale_price=sale_price
    )
    return await food_functions.add_food(request=request, pic=pic, db=db)


@router.put('/update_food', status_code=200, response_model=FoodDisplay)
async def update_food(request: UpdateFoodModel, db: DB_DEPENDENCY):
    return await food_functions.update_food(request=request, db=db)


@router.delete('/delete_food', status_code=200)
async def delete_food(food_id: ID_BODY, db: DB_DEPENDENCY):
    return await food_functions.delete_food(food_id=food_id, db=db)


@router.delete('/delete_all_foods_of_category', status_code=200)
async def delete_all_foods_of_category(category_id: ID_BODY, db: DB_DEPENDENCY):
    return await food_functions.delete_all_foods_of_category(category_id=category_id, db=db)

from database.models import Food
from sqlalchemy.orm import Session
from sqlalchemy import delete, and_
from errors.food_errors import NO_FOOD_FOUND_ERROR, FOOD_NOT_FOUND_ERROR
from schemas.food_schemas import AddFoodModel, UpdateFoodModel, CategoryOnSale




async def add_food(request: AddFoodModel, db: Session):
    ...


async def update_food(request: UpdateFoodModel, db: Session):
    ...


async def delete_food(food_id: int, db: Session):
    ...


async def delete_all_foods_of_category(category_id: int, db: Session):
    ...


async def put_category_on_sale(request: CategoryOnSale, db: Session):
    ...


async def get_food(food_id: int, db: Session):
    ...


async def get_all_foods(db: Session):
    ...


async def get_foods_of_category(category_id: int, db: Session):
    ...


async def get_all_on_sale_foods(db: Session):
    ...


async def get_all_on_sale_foods_of_category(category_id: int, db: Session):
    ...


async def get_all_not_on_sale_foods_of_category(category_id: int, db: Session):
    ...


async def show_coategory_foods(category_id: int, db: Session):
    ...


async def search_food(search: str, db: Session):
    ...


async def get_food_list_by_id(id_list: list[int], db: Session):
    ...


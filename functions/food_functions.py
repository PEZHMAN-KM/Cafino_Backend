from database.models import Food
from sqlalchemy.orm import Session
from fastapi import UploadFile
from sqlalchemy import delete, and_
from errors.food_errors import NO_FOOD_FOUND_ERROR, FOOD_NOT_FOUND_ERROR
from schemas.food_schemas import AddFoodModel, UpdateFoodModel, CategoryOnSale
import random
import shutil
from string import ascii_letters
import os



async def add_food(request: AddFoodModel, db: Session, pic: UploadFile | None = None):
    food = Food(
        name=request.name,
        price=request.price,
        description=request.description,
        category_id=request.category_id,
    )

    db.add(food)
    db.commit()

    if pic:
        rand_str = ''.join(random.choice(ascii_letters) for _ in range(10))
        new_name = f'_{rand_str}.'.join(pic.filename.rsplit('.', 1))
        path_file = f'pictures/{new_name}'

        with open(path_file, 'w+b') as buffer:
            shutil.copyfileobj(pic.file, buffer)

        food.pic_url = path_file
        db.commit()


    return food


async def update_food(request: UpdateFoodModel, db: Session):
    food = db.query(Food).filter(Food.id == request.food_id).first()

    if not food:
        raise FOOD_NOT_FOUND_ERROR

    if request.name:
        food.name = request.name
    if request.price:
        food.price = request.price
    if request.description:
        food.description = request.description
    if request.category_id:
        food.category_id = request.category_id
    if request.in_sale:
        food.in_sale = request.in_sale
    if request.sale_price:
        food.sale_price = request.sale_price

    db.commit()
    db.refresh(food)

    return food


async def delete_food(food_id: int, db: Session):
    food = db.query(Food).filter(Food.id == food_id).first()

    if not food:
        raise NO_FOOD_FOUND_ERROR

    if food.pic_url:
        os.remove(food.pic_url)

    db.delete(food)
    db.commit()

    return f"Food {food.name} Deleted"



async def delete_all_foods_of_category(category_id: int, db: Session):
    delete_food = delete(Food).where(Food.category_id == category_id)
    db.execute(delete_food)

    db.commit()

    return f"Category Foods Deleted"


async def put_category_on_sale(request: CategoryOnSale, db: Session):
    foods = db.query(Food).filter(Food.category_id == request.category_id).all()

    for food in foods:
        food.in_sale = True
        food.sale_price = abs(food.price * (100 - request.discount))

    db.commit()

    return f"Category {request.category_name} On Sale For {request.discount}%"



async def get_food(food_id: int, db: Session):
    food = db.query(Food).filter(Food.id == food_id).first()

    if not food:
        raise FOOD_NOT_FOUND_ERROR

    return food


async def get_all_foods(db: Session):
    foods = db.query(Food).all()

    if not foods:
        raise NO_FOOD_FOUND_ERROR

    return foods


async def get_foods_of_category(category_id: int, db: Session):
    foods = db.query(Food).filter(Food.category_id == category_id).all()

    if not foods:
        raise NO_FOOD_FOUND_ERROR

    return foods


async def get_all_on_sale_foods(db: Session):
    foods = db.query(Food).filter(Food.in_sale == True).all()

    if not foods:
        raise NO_FOOD_FOUND_ERROR

    return foods


async def get_all_on_sale_foods_of_category(category_id: int, db: Session):
    foods = db.query(Food).filter(and_(Food.category_id == category_id, Food.in_sale == True)).all()

    return foods


async def get_all_not_on_sale_foods_of_category(category_id: int, db: Session):
    foods = db.query(Food).filter(and_(Food.category_id == category_id, Food.in_sale == False)).all()

    return foods


async def show_category_foods(category_id: int, db: Session):
    on_sale_foods = get_all_on_sale_foods_of_category(category_id, db)
    not_on_sale_foods = get_all_not_on_sale_foods_of_category(category_id, db)

    category_foods_display = {
        'on_sale_food': on_sale_foods,
        'not_on_sale_food': not_on_sale_foods
    }

    if not category_foods_display:
        raise NO_FOOD_FOUND_ERROR

    return category_foods_display


async def search_food(search: str, db: Session):
    foods = db.query(Food).filter(Food.name.contains(search)).all()

    if not foods:
        raise NO_FOOD_FOUND_ERROR

    return foods


async def get_food_list_by_id(id_list: list[int], db: Session):
    foods = db.query(Food).filter(Food.id.in_(id_list)).all()

    if not foods:
        raise NO_FOOD_FOUND_ERROR

    return foods


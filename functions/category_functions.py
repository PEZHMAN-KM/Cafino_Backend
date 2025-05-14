from database.models import Category, Food
from sqlalchemy.orm import Session
from sqlalchemy import delete, and_
from hash.hash import Hash
from errors.category_errors import CATEGORY_NOT_FOUND_ERROR, CATEGORY_ALREADY_EXISTS_ERROR, NO_CATEGORY_FOUND_ERROR
from schemas.category_schema import UpdateCategoryModel



async def add_category(name: str, db: Session):
    existing_category = db.query(Category).filter(Category.name == name).first()
    if existing_category:
        raise CATEGORY_ALREADY_EXISTS_ERROR  

    category = Category(name=name)
    db.add(category)
    db.commit()
    db.refresh(category)

    return category



async def update_category(info: UpdateCategoryModel, db: Session):
    category = db.query(Category).filter(Category.id == info.id).first()

    if not category:
        raise CATEGORY_NOT_FOUND_ERROR 
    

    existing_category = db.query(Category).filter(Category.name == info.new_name).first()
    if existing_category:
        raise CATEGORY_ALREADY_EXISTS_ERROR  

    category.name = info.new_name

    db.commit()
    db.refresh(category)

    return category



async def delete_category(category_id: int, db: Session):
    category = db.query(Category).filter(Category.id == category_id).first()

    if not category:
        raise CATEGORY_NOT_FOUND_ERROR 
    

    delete_food = delete(Food).where(Food.category_id == category_id)


    db.delete(category)
    db.execute(delete_food)
    db.commit()

    return f"Categoty {category.name} Deleted"


async def get_all_categories(db: Session):
    categories = db.query(Category).all()

    if not categories: 
        raise NO_CATEGORY_FOUND_ERROR
    
    return categories


async def get_category(category_id: int, db: Session):
    category = db.query(Category).filter(Category.id == category_id).first()

    if not category:
        raise CATEGORY_NOT_FOUND_ERROR

    return category

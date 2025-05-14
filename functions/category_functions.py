from database.models import Category
from sqlalchemy.orm import Session
from sqlalchemy import delete, and_
from hash.hash import Hash
from errors.category_errors import CATEGORY_NOT_FOUND_ERROR, NO_CATEGORY_FOUND_ERROR
from schemas.category_schema import UpdateCategoryModel



async def add_category(name: str, db: Session):
    ...


async def update_category(info: UpdateCategoryModel, db: Session):
    ...


async def delete_category(category_id: int, db: Session):
    ...


async def get_all_categories(db: Session):
    ...


async def get_category(category_id: int, db: Session):
    ...
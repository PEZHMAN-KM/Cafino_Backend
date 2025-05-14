from database.models import User
from sqlalchemy.orm import Session
from sqlalchemy import delete, and_
from hash.hash import Hash
from errors.user_errors import (
    USER_NOT_FOUND_ERROR,
    USER_NAME_DUPLICATE_ERROR,
    EMAIL_DUPLICATE_ERROR,
    PHONE_NUMBER_DUPLICATE_ERROR,
    NO_USER_FOUND_ERROR,
    DONT_HAVE_ACCESS_ADMIN_ERROR,
    USER_IS_ALREADY_SELLER_ERROR
)
from functions.general_functions import check_username_duplicate
from schemas.user_schemas import UserModel, UpdateUserModel


async def get_user_by_username(username: str, db: Session):
    user = db.query(User).filter(User.username == username).first()

    if not user:
        raise USER_NOT_FOUND_ERROR

    return user


async def create_user(request: UserModel, db: Session):
    if check_username_duplicate(request.username, db):
        raise USER_NAME_DUPLICATE_ERROR


    user = User(
        username=request.username,
        password=Hash.bcrypt(request.password),
        full_name=request.full_name,
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


async def create_admin(request: UserModel, db: Session):
    ...





async def create_waitress(request: UserModel, db: Session):
    ...


async def update_user(reques: UpdateUserModel, db: Session):
    ...

async def update_self_waitress(reques: UpdateUserModel, db: Session):
    ...

async def update_self_admin(request:UpdateUserModel , db: Session):
    ...


async def update_user_super_admin(request: UpdateUserModel, db: Session):
    ...


async def delete_user(user_id: int, db: Session):
    ...


async def unemploy_user(user_id: int, db: Session):
    ...


async def waitress_self_unemplyment(user_id: int, db: Session):
    ...


async def admin_unemploy_user(user_id: int, db: Session):
    ...


async def super_admin_unemploy_user(user_id: int, db: Session):
    ...


async def get_all_waitresses(db: Session):
    ...


async def get_all_users(db: Session):
    ...


async def get_self_info(user_id: int, db: Session):
    ...
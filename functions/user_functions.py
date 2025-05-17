from database.models import User, Order, Notification
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
    USER_IS_ALREADY_SELLER_ERROR,
    USER_UPDATE_ACCESS_ERROR
)
from functions.general_functions import check_username_duplicate
from schemas.user_schemas import UserModel, UpdateUserModel, AdminUpdateModel


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
        full_name=request.full_name if request.full_name else None,
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


async def create_admin(request: UserModel, db: Session):
    if check_username_duplicate(request.username, db):
        raise USER_NAME_DUPLICATE_ERROR

    user = User(
        username=request.username,
        password=Hash.bcrypt(request.password),
        full_name=request.full_name,
        is_admin=True, 
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


async def create_waitress(request: UserModel, db: Session):
    if check_username_duplicate(request.username, db):
        raise USER_NAME_DUPLICATE_ERROR

    user = User(
        username=request.username,
        password=Hash.bcrypt(request.password),
        full_name=request.full_name,
        is_waitress=True,  # ویترس بودن را مشخص می‌کند
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user



async def update_self_user(request: UpdateUserModel, user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise USER_NOT_FOUND_ERROR

    if request.username:
        user.username = request.username
    if request.password:
        user.password = Hash.bcrypt(request.password)
    if request.full_name:
        user.full_name = request.full_name
    if request.pic_url:
        user.pic_url = request.pic_url

    db.commit()
    db.refresh(user)

    return user
    
    

async def update_by_admin(request: AdminUpdateModel, db: Session):
    user = db.query(User).filter(User.id == request.user_id).first()

    if user.is_admin or not user.is_waitress:
        raise USER_UPDATE_ACCESS_ERROR

    if not user:
        raise USER_NOT_FOUND_ERROR

    if request.username:
        user.username = request.username
    if request.password:
        user.password = Hash.bcrypt(request.password)
    if request.full_name:
        user.full_name = request.full_name
    if request.pic_url:
        user.pic_url = request.pic_url

    db.commit()
    db.refresh(user)

    return user
    


async def update_user_super_admin(request: AdminUpdateModel, db: Session):
    user = db.query(User).filter(User.id == request.user_id).first()

    if not user:
        raise USER_NOT_FOUND_ERROR

    if request.username:
        user.username = request.username
    if request.password:
        user.password = Hash.bcrypt(request.password)
    if request.full_name:
        user.full_name = request.full_name
    if request.pic_url:
        user.pic_url = request.pic_url

    db.commit()
    db.refresh(user)

    return user
    


async def delete_user(user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise USER_NOT_FOUND_ERROR
    

    delete_notifs = delete(Notification).where(Notification.waitress_id == user.id)
    delete_order = delete(Order).where(Order.admin_id== user.id)



    db.delete(user)

    db.execute(delete_notifs)
    db.execute(delete_order)
    db.commit()


    return f'User {user.full_name if user.full_name else user.username} Deleted'


async def admin_unemploy_user(user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise USER_NOT_FOUND_ERROR
    
    if user.is_admin:
        raise USER_UPDATE_ACCESS_ERROR

    user.is_working = False
    db.commit()
    db.refresh(user)

    return user


async def super_admin_unemploy_user(user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise USER_NOT_FOUND_ERROR

    user.is_working = False
    db.commit()
    db.refresh(user)

    return user


async def self_unemplyment(user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise USER_NOT_FOUND_ERROR

    user.is_working = False
    db.commit()
    db.refresh(user)

    return user



async def get_all_waitresses(db: Session):
    waitresses = db.query(User).filter(User.is_waitress == True).all()

    if not waitresses:
        raise NO_USER_FOUND_ERROR
    
    return waitresses


async def get_all_users(db: Session):
    users = db.query(User).all()

    if not users: 
        raise NO_USER_FOUND_ERROR
    
    return users

    


async def get_self_info(user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise USER_NOT_FOUND_ERROR

    return user


async def get_user(user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise USER_NOT_FOUND_ERROR

    return user
import os
import random
import shutil
from fastapi.responses import FileResponse
from string import ascii_letters
from fastapi import UploadFile
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
    USER_UPDATE_ACCESS_ERROR,
    PIC_NOT_FOUND_ERROR
)
from functions.general_functions import check_username_duplicate
from schemas.user_schemas import UserModel, UpdateUserModel, AdminUpdateModel


async def get_user_by_username(username: str, db: Session):
    user = db.query(User).filter(User.username == username).first()

    if not user:
        raise USER_NOT_FOUND_ERROR

    return user


async def create_super_admin(request: UserModel, db: Session):
    if check_username_duplicate(request.username, db):
        raise USER_NAME_DUPLICATE_ERROR


    user = User(
        username=request.username,
        password=Hash.bcrypt(request.password),
        full_name=request.full_name if request.full_name else None,
        is_admin=True,
        is_super_admin=True
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


async def update_user_pic(user_id: int, pic: UploadFile, db: Session):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise USER_NOT_FOUND_ERROR

    old_pic_url: str | None = None

    if user.pic_url:
        old_pic_url = user.pic_url

    rand_str = ''.join(random.choice(ascii_letters) for _ in range(10))
    new_name = f'_{rand_str}.'.join(pic.filename.rsplit('.', 1))
    path_file = f'pictures/{new_name}'

    with open(path_file, 'w+b') as buffer:
        shutil.copyfileobj(pic.file, buffer)

    user.pic_url = path_file

    if old_pic_url:
        os.remove(old_pic_url)


    db.commit()

    return user


async def delete_user_pic(user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise USER_NOT_FOUND_ERROR

    if user.pic_url:
        os.remove(user.pic_url)
        user.pic_url = None

    db.commit()

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


    waitress_in_progress_notifs = db.query(Notification).filter(and_(Notification.waitress_id == user_id, Notification.is_in_progress == True, Notification.is_done == False)).all()

    if waitress_in_progress_notifs:
        for notif in waitress_in_progress_notifs:
            notif.is_in_progress = False
            notif.waitress_id = None
            notif.waitress_name = None
            notif.start_progress_time = None

            db.flush()


    user.is_working = False
    db.commit()
    db.refresh(user)

    return user


async def super_admin_unemploy_user(user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise USER_NOT_FOUND_ERROR


    if user.is_waitress:
        waitress_in_progress_notifs = db.query(Notification).filter(and_(Notification.waitress_id == user_id, Notification.is_in_progress == True, Notification.is_done == False)).all()
        if waitress_in_progress_notifs:
            for notif in waitress_in_progress_notifs:
                notif.is_in_progress = False
                notif.waitress_id = None
                notif.waitress_name = None
                notif.start_progress_time = None

                db.flush()


    if user.is_admin:
        admin_in_progress_orders = db.query(Order).filter(and_(Order.admin_id == user_id, Order.is_in_progress == True, Order.is_done == False)).all()
        if admin_in_progress_orders:
            for order in admin_in_progress_orders:
                order.is_in_progress = False
                order.admin_id = None
                order.admin_name = None
                order.start_progress_time = None

                db.flush()


    user.is_working = False
    db.commit()
    db.refresh(user)

    return user


async def self_unemplyment(user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise USER_NOT_FOUND_ERROR


    if user.is_waitress:
        waitress_in_progress_notifs = db.query(Notification).filter(and_(Notification.waitress_id == user_id, Notification.is_in_progress == True, Notification.is_done == False)).all()
        if waitress_in_progress_notifs:
            for notif in waitress_in_progress_notifs:
                notif.is_in_progress = False
                notif.waitress_id = None
                notif.waitress_name = None
                notif.start_progress_time = None

                db.flush()


    if user.is_admin:
        admin_in_progress_orders = db.query(Order).filter(and_(Order.admin_id == user_id, Order.is_in_progress == True, Order.is_done == False)).all()
        if admin_in_progress_orders:
            for order in admin_in_progress_orders:
                order.is_in_progress = False
                order.admin_id = None
                order.admin_name = None
                order.start_progress_time = None

                db.flush()

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


async def get_user_pic(user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise USER_NOT_FOUND_ERROR

    pic = user.pic_url

    if not pic:
        raise PIC_NOT_FOUND_ERROR

    return FileResponse(path=pic)
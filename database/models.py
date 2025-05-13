from database.database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, Float, JSON


# ID Class ==============================================================================================
class ID:
    __abstract__ = True
    id = Column(Integer, unique=True, index=True, primary_key=True)


# User Class ================================================================================================
class User(ID, Base):
    __tablename__ = "user"
    username = Column(String(150), unique=True, nullable=False)
    password = Column(String(150), nullable=False)
    full_name = Column(String(150), nullable=False)
    pic_url = Column(String, nullable=True)
    is_admin = Column(Boolean, default=False)
    is_super_admin = Column(Boolean, default=False)
    is_waitress = Column(Boolean, default=False)


class Notification(ID, Base):
    __tablename__ = 'notification'
    table_number = Column(Integer, nullable=False)
    add_time = Column(DateTime, nullable=False)
    message = Column(String, nullable=True)
    is_in_progress = Column(Boolean, default=False)
    start_progress_time = Column(DateTime, nullable=True)
    is_done = Column(Boolean, default=False)
    done_time = Column(DateTime, nullable=True)
    waitress_id = Column(Integer, ForeignKey('user.id'), nullable=True)
    waitress_name = Column(String(150), nullable=True)



class Category(ID, Base):
    __tablename__ = 'category'
    name = Column(String(150), nullable=False, unique=True)
    pic_url = Column(String, nullable=True)



class Food(ID, Base):
    __tablename__ = 'food'
    name = Column(String(150), nullable=False)
    price = Column(Integer, nullable=False)
    description = Column(String, nullable=True)
    in_sale = Column(Boolean, default=False)
    sale_price = Column(Integer, nullable=True)
    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)
    pic_url = Column(String, nullable=True)


class Order(ID, Base):
    __tablename__ = 'order'
    table_number = Column(Integer, nullable=False)
    message = Column(String, nullable=True)
    time_added = Column(DateTime, nullable=False)
    is_accepted = Column(Integer, default=False)
    accepted_time = Column(DateTime, nullable=True)
    is_done = Column(Boolean, default=False)
    done_time = Column(DateTime, nullable=True)
    total_price = Column(Integer, nullable=True)
    admin_id = Column(Integer, ForeignKey('user.id'), nullable=True)
    admin_name = Column(String(150), nullable=True)


class OrderFood(ID, Base):
    __tablename__ = 'order_food'
    order_id = Column(Integer, ForeignKey('order.id'), nullable=False)
    food_id = Column(Integer, ForeignKey('food.id'), nullable=False)
    food_price = Column(Integer, nullable=True)
    quantity = Column(Integer, default=1)

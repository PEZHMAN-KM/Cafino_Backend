from database.models import Order
from sqlalchemy.orm import Session
from sqlalchemy import delete, and_
from errors.order_errors import NO_ORDER_FOUND_ERROR, ORDER_NOT_FOUND_ERROR
from schemas.order_schemas import AddOrderModel


async def add_order(request: AddOrderModel, db: Session):
    ...


async def get_order(order_id: int, db: Session):
    ...


async def deny_order(order_id: int, db: Session):
    ...


async def accept_order(order_id: int, db: Session):
    ...


async def get_order_done(order_id: int, db: Session):
    ...


async def get_all_not_accepted_orders(db: Session):
    ...


async def get_all_in_progress_order(db: Session):
    ...


async def get_orders_to_show(db: Session):
    ...

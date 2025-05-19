import datetime
from database.models import Order, OrderFood, Food, User
from sqlalchemy.orm import Session
from sqlalchemy import delete, and_
from errors.order_errors import NO_ORDER_FOUND_ERROR, ORDER_NOT_FOUND_ERROR
from errors.user_errors import USER_NOT_FOUND_ERROR
from schemas.order_schemas import AddOrderModel


async def add_order(request: AddOrderModel, db: Session):
    order = Order(
        table_number=request.table_number,
        message=request.message,
        time_added=datetime.datetime.now()
    )

    db.add(order)

    total_price = 0

    order_foods = []

    for food in request.foods:
        order_food = OrderFood(
            order_id=order.id,
            food_id=food.food_id,
            quantity=food.quantity,
            food_price=food.food_price
        )
        db.add(order_food)

        total_price = total_price + (food.quantity * food.food_price)
        this_food = db.query(Food).filter(Food.id == food.food_id).first()

        this_food.quantity = food.quantity
        order_foods.append(this_food)


    order.total_price = total_price
    db.commit()
    db.refresh(order)



    display_order = {
        "order": order,
        "foods": order_foods
    }

    return display_order



async def get_order(order_id: int, db: Session):
    order = db.query(Order).filter(Order.id == order_id).first()

    if not order:
        raise ORDER_NOT_FOUND_ERROR

    order_foods = db.query(OrderFood).filter(OrderFood.order_id == order_id).all()

    order_foods_display = []

    for find_food in order_foods:
        this_food = db.query(Food).filter(Food.id == find_food.food_id).first()
        this_food.quantity = find_food.quantity
        order_foods_display.append(this_food)

    display_order = {
        "order": order,
        "foods": order_foods_display
    }

    return display_order


async def get_order_to_use(order_id: int, db: Session):
    order = db.query(Order).filter(Order.id == order_id).first()
    order_foods = db.query(OrderFood).filter(OrderFood.order_id == order_id).all()
    order_foods_display = []

    for find_food in order_foods:
        this_food = db.query(Food).filter(Food.id == find_food.food_id).first()
        this_food.quantity = find_food.quantity
        order_foods_display.append(this_food)

    display_order = {
        "order": order,
        "foods": order_foods_display
    }

    return display_order


async def deny_order(order_id: int, db: Session):
    order = db.query(Order).filter(Order.id == order_id).first()

    if not order:
        raise NO_ORDER_FOUND_ERROR

    db.delete(order)
    db.commit()

    return "Order Denied"


async def accept_order(order_id: int, admin_id: int, db: Session):
    order = db.query(Order).filter(Order.id == order_id).first()

    if not order:
        raise ORDER_NOT_FOUND_ERROR

    admin = db.query(User).filter(and_(User.id == admin_id, User.is_admin == True)).first()

    if not admin:
        raise USER_NOT_FOUND_ERROR

    order.is_accepted = True
    order.accepted_time = datetime.datetime.now()
    order.admin_id = admin.id
    order.admin_name = admin.full_name
    db.commit()

    return "Order Accepted"


async def get_order_done(order_id: int, db: Session):
    order = db.query(Order).filter(Order.id == order_id).first()

    if not order:
        raise ORDER_NOT_FOUND_ERROR

    order.is_done = True
    order.done_time = datetime.datetime.now()
    db.commit()

    return "Order Done"


async def get_all_not_accepted_orders(db: Session):
    orders = db.query(Order).filter(and_(Order.is_accepted == False, Order.is_done == False)).all()

    display_orders = []

    for order in orders:
        this_order = await get_order_to_use(order.id, db)
        display_orders.append(this_order)

    return display_orders



async def get_all_in_progress_order(db: Session):
    orders = db.query(Order).filter(and_(Order.is_accepted == True, Order.is_done == False)).all()

    display_orders = []

    for order in orders:
        this_order = await get_order_to_use(order.id, db)
        display_orders.append(this_order)

    return display_orders


async def get_orders_to_show(db: Session):
    not_accepted_orders = await get_all_not_accepted_orders(db)
    in_progress_orders = await get_all_in_progress_order(db)

    display_orders = {
        "not_accepted_orders": not_accepted_orders,
        "in_progress_orders": in_progress_orders
    }

    return display_orders

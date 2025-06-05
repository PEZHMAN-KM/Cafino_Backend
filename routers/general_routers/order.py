from fastapi import APIRouter
from functions import order_functions
from dependencies.dependencies import DB_DEPENDENCY
from dependencies.body_dependencies import ID_BODY
from dependencies.access_dependencies import USER_DEPENDENCY
from schemas.order_schemas import AddOrderModel, OrderShowDisplay, OrdersToShow


router = APIRouter(
    prefix='/order',
    tags=['Order']
)


@router.post('/add_order', status_code=201, response_model=OrderShowDisplay)
async def add_order(request: AddOrderModel, db: DB_DEPENDENCY):
    return await order_functions.add_order(request=request, db=db)


@router.post('/get_order', status_code=200, response_model=OrderShowDisplay)
async def get_order(order_id: ID_BODY, db: DB_DEPENDENCY):
    return await order_functions.get_order(order_id=order_id, db=db)


@router.get('/get_orders_to_show', status_code=200, response_model=OrdersToShow)
async def get_orders_to_show(db: DB_DEPENDENCY):
    return await order_functions.get_orders_to_show(db=db)
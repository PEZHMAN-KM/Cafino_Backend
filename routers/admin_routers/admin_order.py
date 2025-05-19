from fastapi import APIRouter
from schemas.order_schemas import OrderShowDisplay, OrdersToShow
from functions import order_functions
from dependencies.dependencies import DB_DEPENDENCY
from dependencies.body_dependencies import ID_BODY
from dependencies.access_dependencies import ROUTER_ADMIN_DEPENDENCY, ADMIN_DEPENDENCY


router = APIRouter(
    prefix='/admin/notification',
    tags=['Admin Notification'],
    dependencies=[ROUTER_ADMIN_DEPENDENCY]
)


@router.delete('/deny_order', status_code=200)
async def deny_order(order_id: ID_BODY, db: DB_DEPENDENCY):
    return await order_functions.deny_order(order_id=order_id, db=db)


@router.put('/accept_order', status_code=200, response_model=OrderShowDisplay)
async def accept_order(order_id: ID_BODY, admin: ADMIN_DEPENDENCY, db: DB_DEPENDENCY):
    return await order_functions.accept_order(order_id=order_id, admin_id=admin.id, db=db)




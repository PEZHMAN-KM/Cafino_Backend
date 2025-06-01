import datetime

from schemas.base_schemas import BaseSchema
from schemas.food_schemas import FoodDisplay



class OrderFoodModel(BaseSchema):
    food_id: int
    quantity: int


class AddOrderModel(BaseSchema):
    foods: list[OrderFoodModel]
    table_number: int
    message: str | None = None


class OrderFoodDisplay(FoodDisplay):
    quantity: int


class OrderDisplay(BaseSchema):
    id: int
    table_number: int
    message: str | None = None
    total_price: int
    time_added: datetime.datetime
    admin_id: int | None = None
    admin_name: str | None = None
    is_accepted: bool | None = False
    accepted_time: datetime.datetime | None = None
    is_done: bool | None = False
    done_time: datetime.datetime | None = None

class OrderShowDisplay(BaseSchema):
    order: OrderDisplay
    foods: list[OrderFoodDisplay]


class OrdersToShow(BaseSchema):
    not_accepted_orders: list[OrderShowDisplay] | None = None
    in_progress_orders: list[OrderShowDisplay] | None = None
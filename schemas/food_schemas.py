from schemas.base_schemas import BaseSchema


class AddFoodModel(BaseSchema):
    name: str
    price: int
    description: str | None = None
    category_id: int
    in_sale: bool | None = None
    sale_price: int | None = None


class UpdateFoodModel(AddFoodModel):
    food_id: int
    name: str | None = None
    price: int | None = None
    description: str | None = None
    category_id: int | None = None
    in_sale: bool | None = None
    sale_price: int | None = None


class CategoryOnSale(BaseSchema):
    category_id: int
    discount: int


class FoodDisplay(AddFoodModel):
    id: int
    pic_url: str | None


class ShowFoodsOfCategory(BaseSchema):
    on_sale_food: list[FoodDisplay] | None = None
    not_on_sale_food: list[FoodDisplay] | None = None
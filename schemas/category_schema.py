from schemas.base_schemas import BaseSchema



class CategoryDisplay(BaseSchema):
    id: int
    name: str


class UpdateCategoryModel(BaseSchema):
    id: int 
    new_name: str
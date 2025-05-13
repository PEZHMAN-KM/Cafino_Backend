from schemas.base_schemas import BaseSchema


class UserDisplay(BaseSchema):
    username: str
    full_name: str
    pic_url: str | None = None
    is_admin: bool
    is_super_admin: bool
    is_waitress: bool



class UserModel(BaseSchema):
    username: str
    password: str
    full_name: str | None = None


class UserAuth(BaseSchema):
    id: int
    username: str
    phone_number: str | None = None
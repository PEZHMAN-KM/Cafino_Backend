from pydantic import BaseModel


class BaseSchema(BaseModel):
    class Config:
        from_attributes = True
        extra = 'ignore'
        validate_assignment = True

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
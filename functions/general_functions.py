from database.models import User
from sqlalchemy.orm import Session



def check_username_duplicate(username: str, db: Session):
    user = db.query(User).filter(User.username == username).first()

    if user:
        return True
    else:
        return False









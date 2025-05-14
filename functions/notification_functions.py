from database.models import Notification
from sqlalchemy.orm import Session
from sqlalchemy import delete, and_
from errors.notification_errors import NOTIFICATION_NOT_FOUND_ERROR, NO_NOTIFICATION_FOUND_ERROR
from schemas.notification_schemas import AddNotificationModel, UnprogressNotificationModel



async def add_notif(notif: AddNotificationModel, db: Session):
    ...


async def get_notif_in_progress(waitress_id: int, db: Session):
    ...


async def get_out_of_progress(request: UnprogressNotificationModel, db: Session):
    ...


async def get_notif_done(request: UnprogressNotificationModel, db: Session):
    ...


async def get_all_not_done_notifs(db: Session):
    ...


async def get_all_in_progrees_notifs(db: Session):
    ...


async def get_notifs_to_show(db: Session):
    ...


async def get_notif(notif_id: int, db: Session):
    ...

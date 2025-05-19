import datetime

from database.models import Notification, User
from sqlalchemy.orm import Session
from sqlalchemy import delete, and_
from errors.notification_errors import NOTIFICATION_NOT_FOUND_ERROR, NO_NOTIFICATION_FOUND_ERROR
from errors.user_errors import USER_NOT_FOUND_ERROR
from schemas.notification_schemas import AddNotificationModel, GetNotifInProgress



async def add_notif(notif: AddNotificationModel, db: Session):
    new_notif = Notification(
        table_number=notif.table_number,
        add_time=datetime.datetime.now(),
        message=notif.message if notif.message else None
    )

    db.add(new_notif)
    db.commit()
    db.refresh(new_notif)

    return new_notif


async def get_notif_in_progress(request: GetNotifInProgress, db: Session):
    notif = db.query(Notification).filter(Notification.id == request.notif_id).first()

    if not notif:
        raise NOTIFICATION_NOT_FOUND_ERROR

    waitress = db.query(User).filter(and_(User.id == request.waitress_id, User.is_waitress == True)).first()

    if not waitress:
        raise USER_NOT_FOUND_ERROR

    notif.in_progress = True
    notif.waitress_id = request.waitress_id
    notif.waitress_name = waitress.full_name
    notif.start_progress_time = datetime.datetime.now()
    db.commit()


    return notif



async def get_out_of_progress(notif_id: int, db: Session):
    notif = db.query(Notification).filter(Notification.id == notif_id).first()

    if not notif:
        raise NOTIFICATION_NOT_FOUND_ERROR

    notif.in_progress = False
    notif.waitress_id = None
    notif.waitress_name = None
    notif.start_progress_time = None
    db.commit()

    return notif


async def get_notif_done(notif_id: int, db: Session):
    notif = db.query(Notification).filter(Notification.id == notif_id).first()

    if not notif:
        raise NOTIFICATION_NOT_FOUND_ERROR

    notif.is_done = True
    notif.done_time = datetime.datetime.now()
    db.commit()

    return notif


async def get_all_requested_notifs(db: Session):
    notifs = db.query(Notification).filter(and_(Notification.is_done == False, Notification.is_in_progress == False)).all()

    return notifs


async def get_all_in_progress_notifs(db: Session):
    notifs = db.query(Notification).filter(and_(Notification.is_done == False, Notification.is_in_progress == True)).all()

    return notifs


async def get_notifs_to_show(db: Session):
    in_progress_notifs = get_all_in_progress_notifs(db)
    requested_notifs = get_all_requested_notifs(db)

    if not in_progress_notifs and not requested_notifs:
        raise NO_NOTIFICATION_FOUND_ERROR

    notifs_display = {
        'in_progress_notifs': in_progress_notifs,
        'requested_notifs': requested_notifs
    }


    return notifs_display




async def get_notif(notif_id: int, db: Session):
    notif = db.query(Notification).filter(Notification.id == notif_id).first()

    if not notif:
        raise NOTIFICATION_NOT_FOUND_ERROR

    return notif

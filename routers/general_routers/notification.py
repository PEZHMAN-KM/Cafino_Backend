from fastapi import APIRouter
from functions import notification_functions
from dependencies.dependencies import DB_DEPENDENCY
from dependencies.body_dependencies import ID_BODY
from dependencies.access_dependencies import USER_DEPENDENCY
from schemas.notification_schemas import NotificationDisplay, AddNotificationModel


router = APIRouter(
    prefix='/notification',
    tags=['Notification']
)


@router.post('/add_notif', status_code=201, response_model=NotificationDisplay)
async def add_notif(notif: AddNotificationModel, db: DB_DEPENDENCY):
    return await notification_functions.add_notif(notif=notif, db=db)


@router.put('/get_out_of_progress', status_code=200, response_model=NotificationDisplay)
async def get_out_of_progress(notif_id: ID_BODY, db: DB_DEPENDENCY, user: USER_DEPENDENCY):
    return await notification_functions.get_out_of_progress(notif_id=notif_id, user_id=user.id, db=db)


@router.get('/get_notifs_to_show', status_code=200, response_model=list[NotificationDisplay])
async def get_notifs_to_show(db: DB_DEPENDENCY):
    return await notification_functions.get_notifs_to_show(db=db)


@router.get('get_notif', status_code=200, response_model=NotificationDisplay)
async def get_notif(notif_id: ID_BODY, db: DB_DEPENDENCY):
    return await notification_functions.get_notif(notif_id=notif_id, db=db)
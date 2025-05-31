from fastapi import APIRouter
from schemas.notification_schemas import NotificationDisplay
from functions import notification_functions
from dependencies.dependencies import DB_DEPENDENCY
from dependencies.body_dependencies import ID_BODY
from dependencies.access_dependencies import ROUTER_WAITRESS_DEPENDENCY, WAITRESS_DEPENDENCY


router = APIRouter(
    prefix='/waitress/notification',
    tags=['Waitress Notification'],
    # dependencies=[ROUTER_WAITRESS_DEPENDENCY]
)


@router.put('/get_notif_in_progress', status_code=200, response_model=NotificationDisplay)
async def get_notif_in_progress(notif_id: ID_BODY, db: DB_DEPENDENCY, user: WAITRESS_DEPENDENCY):
    return await notification_functions.get_notif_in_progress(notif_id=notif_id, db=db, waitress_id=user.id)


@router.put('/get_notif_done', status_code=200, response_model=NotificationDisplay)
async def get_notif_done(notif_id: ID_BODY, waitress: WAITRESS_DEPENDENCY, db: DB_DEPENDENCY):
    return await notification_functions.get_notif_done(notif_id=notif_id, waitress_id=waitress.id, db=db)
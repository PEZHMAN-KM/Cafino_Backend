from fastapi import APIRouter
from schemas.notification_schemas import NotificationDisplay
from functions import notification_functions
from dependencies.dependencies import DB_DEPENDENCY
from dependencies.body_dependencies import ID_BODY
from dependencies.access_dependencies import ROUTER_ADMIN_DEPENDENCY


router = APIRouter(
    prefix='/admin/notification',
    tags=['Admin Notification'],
    dependencies=[ROUTER_ADMIN_DEPENDENCY]
)




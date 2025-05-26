import datetime
from schemas.base_schemas import BaseSchema



class AddNotificationModel(BaseSchema):
    table_number: int
    message: str | None = None


class GetNotifInProgress(BaseSchema):
    waitress_id: int
    notif_id: int

class NotificationDisplay(AddNotificationModel):
    id : int
    add_time: datetime.datetime
    is_in_progress: bool
    start_progress_time: datetime.datetime | None = None
    is_done: bool
    done_time: datetime.datetime | None = None
    waitress_id: int | None = None
    waitress_name: str | None = None


class ShowNotifications(BaseSchema):
    in_progress_notifs: list[NotificationDisplay] | None = None
    requested_notifs: list[NotificationDisplay] | None = None
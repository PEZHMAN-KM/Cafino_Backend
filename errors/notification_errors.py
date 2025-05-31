from fastapi.exceptions import HTTPException
from fastapi import status



NOTIFICATION_NOT_FOUND_ERROR = HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                             detail='Notification Not Found')

NO_NOTIFICATION_FOUND_ERROR = HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                            detail='No Notification Found')


NOTIFICATION_IS_NOT_IN_PROGRESS = HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                                detail='Notification Is Not In Progress.')


WAITRESS_NOTIFICATION_ACCESS_ERROR = HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                                   detail="You Can Not Change Other Waitresses Notifs.")
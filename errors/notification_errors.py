from fastapi.exceptions import HTTPException
from fastapi import status



NOTIFICATION_NOT_FOUND_ERROR = HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                             detail='Notification Not Found')

NO_NOTIFICATION_FOUND_ERROR = HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                            detail='No Notification Found')
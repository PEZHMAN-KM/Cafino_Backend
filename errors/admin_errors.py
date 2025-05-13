from fastapi.exceptions import HTTPException
from fastapi import status


USER_IS_ALREADY_ADMIN_ERROR = HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                            detail="User is already an admin")

USER_IS_NOT_ADMIN_ERROR = HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                        detail="User is not an admin")
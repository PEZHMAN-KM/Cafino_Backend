from fastapi.exceptions import HTTPException
from fastapi import status



INTERNAL_ERROR = HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                               detail='Something Went Wrong. Try Again Later.')
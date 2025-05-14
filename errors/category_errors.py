from fastapi.exceptions import HTTPException
from fastapi import status



CATEGORY_NOT_FOUND_ERROR = HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                         detail='Category Not Found')

NO_CATEGORY_FOUND_ERROR = HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                         detail='No Category Found')
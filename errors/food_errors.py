from fastapi.exceptions import HTTPException
from fastapi import status



FOOD_NOT_FOUND_ERROR = HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                     detail='Food Not Found')

NO_FOOD_FOUND_ERROR = HTTPException(status_code=status.HTTP_204_NO_CONTENT,
                                         detail='No Food Found')
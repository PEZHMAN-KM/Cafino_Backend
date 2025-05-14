from fastapi.exceptions import HTTPException
from fastapi import status



ORDER_NOT_FOUND_ERROR = HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                      detail='Order Not Found')

NO_ORDER_FOUND_ERROR = HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                     detail='No Order Found')
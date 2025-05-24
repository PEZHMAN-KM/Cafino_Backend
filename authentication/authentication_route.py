from fastapi import APIRouter
from dependencies.dependencies import AUTHENTICATION_DEPENDENCY, DB_DEPENDENCY, TOKEN_DEPENDENCY
from authentication import access

router = APIRouter(
    prefix='/authentication',
    tags=['Authentication']
)


@router.post('/token')
async def login(request: AUTHENTICATION_DEPENDENCY, db: DB_DEPENDENCY):
    return await access.login(request=request, db=db)


@router.post('/refresh_token')
async def get_new_access_token(token: TOKEN_DEPENDENCY, db: DB_DEPENDENCY):
    return await access.get_new_access_token(token=token, db=db)


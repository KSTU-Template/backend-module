from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from web.database.dals import ClientDAL
from web.database.models import User
from web.database.session import get_db
from web.schemas.client import ClientIn
from web.utils.authentication import get_current_user

router = APIRouter(prefix='/client', tags=['Client'])


@router.get('/')
async def get_clients(session: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    return await ClientDAL.read(session, user_id=current_user.id)


@router.post('/')
async def create_client(
        body: ClientIn, session: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)
):
    return await ClientDAL.create(session, data=body.model_dump(), user_id=current_user.id)


@router.delete('/{client_id}')
async def delete_client(
        client_id: int, session: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)
):
    await ClientDAL.delete(session, user_id=current_user.id, id=client_id)

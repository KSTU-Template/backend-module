from datetime import datetime

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from web.database.dals import ProductDAL
from web.database.models import User
from web.database.session import get_db
from web.utils.authentication import get_current_user

router = APIRouter(prefix='/product', tags=['Product'])


class ProductOut(BaseModel):
    id: int
    name: str
    description: str
    created_at: datetime
    updated_at: datetime


@router.get('/', response_model=list[ProductOut])
async def get_products(session: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    return await ProductDAL.read(session)

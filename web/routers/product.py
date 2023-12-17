from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from web.database.dals import ProductDAL
from web.database.models import User
from web.database.session import get_db
from web.utils.authentication import get_current_user

router = APIRouter(prefix='/product', tags=['Product'])


class ProductOut(BaseModel):
    title: str
    description: str
    interest_rate: str | None = None
    category: str
    advantages: list | None = None
    conditions: str | None = None
    benefits: str | None = None


@router.get('/', response_model=list[ProductOut])
async def get_products(session: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    return await ProductDAL.read(session)

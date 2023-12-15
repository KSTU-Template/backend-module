from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from web.database.dals import ChatDAL
from web.database.models import User
from web.database.session import get_db
from web.schemas.chat import QuestionIn
from web.utils.authentication import get_current_user

router = APIRouter(prefix='/chat', tags=['Chat'])


@router.get("/")
async def get_user_dialog(session: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    return await ChatDAL.read(session, user_id=current_user.id)


@router.post("/")
async def request_offer(
        body: QuestionIn, session: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)
):
    question = await ChatDAL.create(session, **body.model_dump(), user_id=current_user.id)

    # какая-то логика по получению ответа
    ai_answer = 'Привет, это бот, я отвечу на все твои вопросы :)'

    answer = await ChatDAL.create(session, text=ai_answer, question_id=question.id, user_id=current_user.id)

    return answer

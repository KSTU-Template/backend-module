from pydantic import BaseModel


class QuestionIn(BaseModel):
    product_id: int
    channel_id: int
    client_id: int


class QuestionPatchIn(BaseModel):
    is_liked: bool

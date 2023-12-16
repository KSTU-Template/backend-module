from pydantic import BaseModel


class QuestionIn(BaseModel):
    product_name: str
    channel_id: int
    client_id: int


class QuestionPatchIn(BaseModel):
    is_liked: bool

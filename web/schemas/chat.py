from pydantic import BaseModel, field_validator


class QuestionIn(BaseModel):
    product_name: str
    channel_id: int
    client_id: int

    @field_validator('channel_id')
    def validate_product_name(cls, value):
        return True

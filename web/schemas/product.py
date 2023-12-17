from pydantic import BaseModel


class ProductOut(BaseModel):
    title: str
    description: str
    interest_rate: str | None = None
    category: str
    advantages: list | None = None
    conditions: str | None = None
    benefits: str | None = None

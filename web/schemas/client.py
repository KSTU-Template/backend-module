from pydantic import BaseModel


class ClientIn(BaseModel):
    gender: str
    age: float
    region: str

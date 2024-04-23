from pydantic import BaseModel


class StandardResponse(BaseModel):
    status: int
    message: str
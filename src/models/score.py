from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/municipalities/{id}/score",
    tags=["Scoring"]
)


class Score(BaseModel):
    id: int
    score: float
    period: str

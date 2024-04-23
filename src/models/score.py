from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/municipalities/{municipality_id}/score",
    tags=["Scoring"]
)


class Score(BaseModel):
    municipality_id: int
    score: float
    period: str

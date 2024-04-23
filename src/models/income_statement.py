from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/municipalities/{municipality_id}/incomeStatement",
    tags=["Income statements"]
)


class IncomeStatement(BaseModel):
    municipality_id: int
    assets: int
    passives: int
    period: str

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/municipalities/{id}/incomeStatement",
    tags=["Income statements"]
)


class IncomeStatement(BaseModel):
    id: int
    assets: int
    passives: int
    period: str

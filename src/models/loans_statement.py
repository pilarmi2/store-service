from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/municipalities/{id}/loansStatement",
    tags=["Loans statements"]
)


class LoansStatement(BaseModel):
    id: int
    purpose: str
    agreed_amount: int
    drawn_amount: int
    repaid_amount: int
    maturity_date: str
    period: str

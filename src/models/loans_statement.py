from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/municipalities/{municipality_id}/loansStatement",
    tags=["Loans statements"]
)


class LoansStatement(BaseModel):
    municipality_id: int
    purpose: str
    agreed_amount: int
    drawn_amount: int
    repaid_amount: int
    maturity_date: str
    period: str

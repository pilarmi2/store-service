from typing import Annotated

from fastapi import Body

from src.models.loans_statement import router
from src.models.loans_statement import LoansStatement
from src.models.standard_response import StandardResponse


@router.get('')
async def search_loans_statement(
        municipality_id: int,
        period: str
):
    return {"municipality_id": municipality_id,
            "purpose": "Mortgage",
            "agreed_amount": 16461616544,
            "drawn_amount": 16461616544,
            "repaid_amount": 0,
            "maturity_date": "2029-12-31",
            "period": period}


@router.post("")
async def create_loans_statement(
        loans_statement: Annotated[LoansStatement, Body()],
) -> StandardResponse:
    return StandardResponse(status=201, message="Created")

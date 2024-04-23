from typing import Annotated

from fastapi import Body

from src.models.income_statement import router, IncomeStatement
from src.models.standard_response import StandardResponse


@router.get('')
async def search_income_statement(
        id: int,
        period: str
):
    return {"id": id, "assets": 549849616516, "passives": 4611661, "period": period}


@router.post("")
async def create_income_statement(
        income_statement: Annotated[IncomeStatement, Body()],
) -> StandardResponse:
    return StandardResponse(status=201, message="Created")

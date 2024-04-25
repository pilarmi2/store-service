from typing import Annotated

from fastapi import Body

from src.models.income_statement import router, IncomeStatement
from src.models.standard_response import StandardResponse
from src.repository.income_statement_repository import IncomeStatementRepository
from src.repository.repository import Repository

repository: Repository = IncomeStatementRepository()


@router.get('')
async def search_income_statement(
        municipality_id: str,
        period: str
):
    return repository.get_by_id_and_period(municipality_id, period)


@router.post("")
async def create_income_statement(
        municipality_id: str,
        income_statement: Annotated[IncomeStatement, Body()]
) -> StandardResponse:
    if municipality_id != income_statement.municipality_id:
        return StandardResponse(status="400", message="Wrong municipality_id")
    return repository.add_or_update(income_statement)

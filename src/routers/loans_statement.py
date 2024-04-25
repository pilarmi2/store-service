from typing import Annotated

from fastapi import Body

from src.models.loans_statement import router
from src.models.loans_statement import LoansStatement
from src.models.standard_response import StandardResponse
from src.repository.loans_statement_repository import LoansStatementRepository
from src.repository.repository import Repository

repository: Repository = LoansStatementRepository()


@router.get('')
async def search_loans_statement(
        municipality_id: str,
        period: str
):
    return repository.get_by_id_and_period(municipality_id, period)


@router.post("")
async def create_loans_statement(
        municipality_id: str,
        loans_statement: Annotated[LoansStatement, Body()]
) -> StandardResponse:
    if municipality_id != loans_statement.municipality_id:
        return StandardResponse(status="400", message="Wrong municipality_id")
    return repository.add_or_update(loans_statement)

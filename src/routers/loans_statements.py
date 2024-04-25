from typing import Annotated

from fastapi import Body

from src.models.loan_statement import router
from src.models.loan_statement import LoanStatement
from src.models.standard_response import StandardResponse
from src.repository.loan_statement_repository import LoanStatementRepository
from src.repository.repository import Repository

repository: Repository = LoanStatementRepository()


@router.get('')
async def search_loans_statement(
        municipality_id: str,
        period: str
):
    return repository.get_by_id_and_period(municipality_id, period)


@router.post("")
async def create_loans_statement(
        municipality_id: str,
        loan_statement: Annotated[LoanStatement, Body()]
) -> StandardResponse:
    if municipality_id != loan_statement.municipality_id:
        return StandardResponse(status="400", message="Wrong municipality_id")
    return repository.add_or_update(loan_statement)

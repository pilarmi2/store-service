from typing import List

from src.models.loans_statement import LoansStatement
from src.models.standard_response import StandardResponse
from src.repository.repository import Repository


class LoansStatementRepository(Repository):
    def __init__(self):
        self.__loans_statements: List[LoansStatement] = []

    def get_all(self):
        pass

    def get_by_id(self, object_id: int):
        pass

    def get_by_id_and_period(self, object_id: int, period: str):
        return next(
            (loans_statement for loans_statement in self.__loans_statements
             if loans_statement.municipality_id == object_id and loans_statement.period == period),
            None
        )

    def add_or_update(self, entity: LoansStatement):
        loans_statement: LoansStatement = next(
            (loans_statement for loans_statement in self.__loans_statements
             if
             loans_statement.municipality_id == entity.municipality_id and loans_statement.period == entity.period),
            None
        )

        if loans_statement is None:
            self.__loans_statements.append(entity)
            return StandardResponse(status=200, message="Created")
        else:
            loans_statement.municipality_id = entity.municipality_id
            loans_statement.purpose = entity.purpose
            loans_statement.agreed_amount = entity.agreed_amount
            loans_statement.drawn_amount = entity.drawn_amount
            loans_statement.repaid_amount = entity.repaid_amount
            loans_statement.maturity_date = entity.maturity_date
            loans_statement.period = entity.period
            return StandardResponse(status=200,
                                    message=f"Loans statement for municipality_id {loans_statement.municipality_id} "
                                            f"and period {loans_statement.period} updated")

from typing import List

from src.models.income_statement import IncomeStatement
from src.models.standard_response import StandardResponse
from src.repository.repository import Repository


class IncomeStatementRepository(Repository):
    def __init__(self):
        self.__income_statements: List[IncomeStatement] = []

    def get_all(self):
        pass

    def get_by_id(self, object_id: int):
        pass

    def get_by_id_and_period(self, object_id: int, period: str):
        return next(
            (income_statement for income_statement in self.__income_statements
             if income_statement.municipality_id == object_id and income_statement.period == period),
            None
        )

    def add_or_update(self, entity: IncomeStatement):
        income_statement: IncomeStatement = next(
            (income_statement for income_statement in self.__income_statements
             if income_statement.municipality_id == entity.municipality_id and income_statement.period == entity.period),
            None
        )

        if income_statement is None:
            self.__income_statements.append(entity)
            return StandardResponse(status=200, message="Created")
        else:
            income_statement.municipality_id = entity.municipality_id
            income_statement.assets = entity.assets
            income_statement.passives = entity.passives
            income_statement.period = entity.period
            return StandardResponse(status=200,
                                    message=f"Income statement for municipality_id {income_statement.municipality_id} "
                                            f"and period {income_statement.period} updated")

from typing import List

from src.models.income_statement import IncomeStatement
from src.models.standard_response import StandardResponse
from src.repository.repository import Repository


class IncomeStatementRepository(Repository):
    """
    Represents a repository for managing income statements.

    This repository allows for retrieving, adding, and updating income statements.

    Attributes:
        __income_statements (List[IncomeStatement]): A list to store income statements.

    Methods:
        get_by_id_and_period(object_id: str, period: str): Retrieves an income statement by its ID and period.
        add_or_update(entity: IncomeStatement): Adds or updates an income statement.
    """

    def __init__(self):
        self.__income_statements: List[IncomeStatement] = []

    def get_all(self):
        pass  # This method must be implemented due to the abstract class Repository, but is not used.

    def get_by_id(self, object_id: str):
        pass  # This method must be implemented due to the abstract class Repository, but is not used.

    def get_by_id_and_period(self, object_id: str, period: str):
        """
        Retrieves an income statement by its ID and period.

        Args:
            object_id (str): The ID of the income statement to retrieve.
            period (str): The period of the income statement to retrieve.

        Returns:
            IncomeStatement: The income statement with the specified ID and period, if found; otherwise, None.
        """
        return next(
            (income_statement for income_statement in self.__income_statements
             if income_statement.municipality_id == object_id and income_statement.period == period),
            None
        )

    def add_or_update(self, entity: IncomeStatement) -> StandardResponse:
        """
        Adds or updates an income statement.

        If an income statement with the same ID and period already exists, it updates the existing income statement.
        Otherwise, it adds the new income statement to the repository.

        Args:
            entity (IncomeStatement): The income statement to add or update.

        Returns:
            StandardResponse: A standard response indicating the status of the operation.
        """
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

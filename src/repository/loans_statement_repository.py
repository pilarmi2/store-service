from typing import List

from src.models.loans_statement import LoansStatement
from src.models.standard_response import StandardResponse
from src.repository.repository import Repository


class LoansStatementRepository(Repository):
    """
    Represents a repository for managing loans statements.

    This repository allows for retrieving, adding, and updating loans statements.

    Attributes:
        __loans_statements (List[LoansStatement]): A list to store loans statements.

    Methods:
        get_by_id_and_period(object_id: str, period: str): Retrieves a loans statement by its ID and period.
        add_or_update(entity: LoansStatement): Adds or updates a loans statement.
    """

    def __init__(self):
        self.__loans_statements: List[LoansStatement] = []

    def get_all(self):
        pass  # This method must be implemented due to the abstract class Repository, but is not used.

    def get_by_id(self, object_id: str):
        pass  # This method must be implemented due to the abstract class Repository, but is not used.

    def get_by_id_and_period(self, object_id: str, period: str):
        """
        Retrieves a loans statement by its ID and period.

        Args:
            object_id (str): The ID of the loans statement to retrieve.
            period (str): The period of the loans statement to retrieve.

        Returns:
            LoansStatement: The loans statement with the specified ID and period, if found; otherwise, None.
        """
        return next(
            (loans_statement for loans_statement in self.__loans_statements
             if loans_statement.municipality_id == object_id and loans_statement.period == period),
            None
        )

    def add_or_update(self, entity: LoansStatement) -> StandardResponse:
        """
        Adds or updates a loans statement.

        If a loans statement with the same ID and period already exists, it updates the existing loans statement.
        Otherwise, it adds the new loans statement to the repository.

        Args:
            entity (LoansStatement): The loans statement to add or update.

        Returns:
            StandardResponse: A standard response indicating the status of the operation.
        """
        loans_statement: LoansStatement = next(
            (loans_statement for loans_statement in self.__loans_statements
             if loans_statement.municipality_id == entity.municipality_id and loans_statement.period == entity.period),
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

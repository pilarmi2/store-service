from typing import List

from src.models.loan_statement import LoanStatement
from src.models.standard_response import StandardResponse
from src.repository.repository import Repository


class LoanStatementRepository(Repository):
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
        self.__loans_statements: List[LoanStatement] = []

    def get_all(self):
        pass  # This method must be implemented due to the abstract class Repository, but is not used.

    def get_by_id(self, object_id: str):
        pass  # This method must be implemented due to the abstract class Repository, but is not used.

    def get_by_id_and_period(self, object_id: str, period: str):
        """
        Retrieves all loans statements that match the given ID and period.

        Args:
            object_id (str): The ID of the loans statement to retrieve.
            period (str): The period of the loans statement to retrieve.

        Returns:
            List[LoansStatement]: A list of loans statements with the specified ID and period, if found; otherwise, an empty list.
        """
        return [loan_statement for loan_statement in self.__loans_statements
                if loan_statement.municipality_id == object_id and loan_statement.period == period]

    def add_or_update(self, entity: LoanStatement) -> StandardResponse:
        """
        Adds or updates a loans statement.

        If a loans statement with the same ID and period already exists, it updates the existing loans statement.
        Otherwise, it adds the new loans statement to the repository.

        Args:
            entity (LoansStatement): The loans statement to add or update.

        Returns:
            StandardResponse: A standard response indicating the status of the operation.
        """
        loan_statement: LoanStatement = next(
            (loan_statement for loan_statement in self.__loans_statements
             if loan_statement.municipality_id == entity.municipality_id and loan_statement.period == entity.period and
             loan_statement.maturity_date == entity.maturity_date),
            None
        )

        if loan_statement is None:
            self.__loans_statements.append(entity)
            return StandardResponse(status=200, message="Created")
        else:
            loan_statement.municipality_id = entity.municipality_id
            loan_statement.purpose = entity.purpose
            loan_statement.agreed_amount = entity.agreed_amount
            loan_statement.drawn_amount = entity.drawn_amount
            loan_statement.repaid_amount = entity.repaid_amount
            loan_statement.maturity_date = entity.maturity_date
            loan_statement.period = entity.period
            return StandardResponse(status=200,
                                    message=f"Loans statements for municipality_id {loan_statement.municipality_id} "
                                            f"and period {loan_statement.period} updated")

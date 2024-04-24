import unittest

from src.models.loans_statement import LoansStatement
from src.repository.loans_statement_repository import LoansStatementRepository
from src.repository.repository import Repository


class TestLoansStatementRepository(unittest.TestCase):
    def test_add_loans_statement(self):
        repository: Repository = LoansStatementRepository()
        assert repository.get_by_id_and_period(1, "2023-12-31") is None
        repository.add_or_update(
            LoansStatement(municipality_id=1, purpose="Mortgage", agreed_amount=1000, drawn_amount=1000,
                           repaid_amount=500,
                           maturity_date="2025-12-310", period="2023-12-31"))
        assert repository.get_by_id_and_period(1, "2023-12-31").purpose == "Mortgage"

    def test_update_loans_statement(self):
        repository: Repository = LoansStatementRepository()
        repository.add_or_update(
            LoansStatement(municipality_id=1, purpose="Mortgage", agreed_amount=1000, drawn_amount=1000,
                           repaid_amount=500,
                           maturity_date="2025-12-310", period="2023-12-31"))
        assert repository.get_by_id_and_period(1, "2023-12-31").purpose == "Mortgage"
        repository.add_or_update(
            LoansStatement(municipality_id=1, purpose="Loan", agreed_amount=1000, drawn_amount=1000, repaid_amount=500,
                           maturity_date="2025-12-310", period="2023-12-31"))
        assert repository.get_by_id_and_period(1, "2023-12-31").purpose == "Loan"

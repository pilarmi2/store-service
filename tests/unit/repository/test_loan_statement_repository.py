import unittest

from src.models.loan_statement import LoanStatement
from src.repository.loan_statement_repository import LoanStatementRepository
from src.repository.repository import Repository


class TestLoanStatementRepository(unittest.TestCase):
    def test_add_loan_statement(self):
        repository: Repository = LoanStatementRepository()
        assert not repository.get_by_id_and_period("1", "2023-12-31")
        repository.add_or_update(
            LoanStatement(municipality_id="1", purpose="Mortgage", agreed_amount=1000, drawn_amount=1000,
                           repaid_amount=500,
                           maturity_date="2025-12-310", period="2023-12-31"))
        assert repository.get_by_id_and_period("1", "2023-12-31")[0].purpose == "Mortgage"

    def test_update_loan_statement(self):
        repository: Repository = LoanStatementRepository()
        repository.add_or_update(
            LoanStatement(municipality_id="1", purpose="Mortgage", agreed_amount=1000, drawn_amount=1000,
                           repaid_amount=500,
                           maturity_date="2025-12-310", period="2023-12-31"))
        assert repository.get_by_id_and_period("1", "2023-12-31")[0].purpose == "Mortgage"
        repository.add_or_update(
            LoanStatement(municipality_id="1", purpose="Loan", agreed_amount=1000, drawn_amount=1000, repaid_amount=500,
                           maturity_date="2025-12-310", period="2023-12-31"))
        assert repository.get_by_id_and_period("1", "2023-12-31")[0].purpose == "Loan"

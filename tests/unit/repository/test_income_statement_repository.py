from src.models.income_statement import IncomeStatement
from src.repository.income_statement_repository import IncomeStatementRepository
from src.repository.repository import Repository


def test_add_income_statement():
    repository: Repository = IncomeStatementRepository()
    assert repository.get_by_id_and_period(1, "2023-12-31") is None
    repository.add_or_update(IncomeStatement(municipality_id=1, assets=1000, passives=500, period="2023-12-31"))
    assert repository.get_by_id_and_period(1, "2023-12-31").assets == 1000


def test_update_income_statement():
    repository: Repository = IncomeStatementRepository()
    repository.add_or_update(IncomeStatement(municipality_id=1, assets=1000, passives=500, period="2023-12-31"))
    assert repository.get_by_id_and_period(1, "2023-12-31").assets == 1000
    repository.add_or_update(IncomeStatement(municipality_id=1, assets=2000, passives=500, period="2023-12-31"))
    assert repository.get_by_id_and_period(1, "2023-12-31").assets == 2000

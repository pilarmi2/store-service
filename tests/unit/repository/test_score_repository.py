import unittest

from src.models.score import Score
from src.repository.score_repository import ScoreRepository
from src.repository.repository import Repository


class ScoreRepositoryTest(unittest.TestCase):
    def test_add_score(self):
        repository: Repository = ScoreRepository()
        assert repository.get_by_id_and_period("1", "2023-12-31") is None
        repository.add_or_update(Score(municipality_id="1", score=1.68, period="2023-12-31"))
        assert repository.get_by_id_and_period("1", "2023-12-31").score == 1.68

    def test_update_score(self):
        repository: Repository = ScoreRepository()
        repository.add_or_update(Score(municipality_id="1", score=1.68, period="2023-12-31"))
        assert repository.get_by_id_and_period("1", "2023-12-31").score == 1.68
        repository.add_or_update(Score(municipality_id="1", score=3.19, period="2023-12-31"))
        assert repository.get_by_id_and_period("1", "2023-12-31").score == 3.19

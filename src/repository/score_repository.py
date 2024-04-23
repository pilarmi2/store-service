from typing import List

from src.models.score import Score
from src.models.standard_response import StandardResponse
from src.repository.repository import Repository


class ScoreRepository(Repository):
    def __init__(self):
        self.__scores: List[Score] = []

    def get_all(self):
        pass

    def get_by_id(self, object_id: int):
        pass

    def get_by_id_and_period(self, object_id: int, period: str):
        return next(
            (score for score in self.__scores
             if score.municipality_id == object_id and score.period == period),
            None
        )

    def add_or_update(self, entity: Score):
        score: Score = next(
            (score for score in self.__scores
             if
             score.municipality_id == entity.municipality_id and score.period == entity.period),
            None
        )

        if score is None:
            self.__scores.append(entity)
            return StandardResponse(status=200, message="Created")
        else:
            score.municipality_id = entity.municipality_id
            score.score = entity.score
            score.period = entity.period
            return StandardResponse(status=200,
                                    message=f"Score for municipality_id {score.municipality_id} "
                                            f"and period {score.period} updated")

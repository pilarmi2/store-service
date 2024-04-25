from typing import List

from src.models.score import Score
from src.models.standard_response import StandardResponse
from src.repository.repository import Repository


class ScoreRepository(Repository):
    """
    Represents a repository for managing scores.

    This repository allows for retrieving, adding, and updating scores.

    Attributes:
        __scores (List[Score]): A list to store scores.

    Methods:
        get_by_id_and_period(object_id: str, period: str): Retrieves a score by its ID and period.
        add_or_update(entity: Score): Adds or updates a score.
    """

    def __init__(self):
        self.__scores: List[Score] = []

    def get_all(self):
        pass  # This method must be implemented due to the abstract class Repository, but is not used.

    def get_by_id(self, object_id: str):
        pass  # This method must be implemented due to the abstract class Repository, but is not used.

    def get_by_id_and_period(self, object_id: str, period: str):
        """
        Retrieves a score by its ID and period.

        Args:
            object_id (str): The ID of the score to retrieve.
            period (str): The period of the score to retrieve.

        Returns:
            Score: The score with the specified ID and period, if found; otherwise, None.
        """
        return next(
            (score for score in self.__scores
             if score.municipality_id == object_id and score.period == period),
            None
        )

    def add_or_update(self, entity: Score):
        """
        Adds or updates a score.

        If a score with the same ID and period already exists, it updates the existing score.
        Otherwise, it adds the new score to the repository.

        Args:
            entity (Score): The score to add or update.

        Returns:
            StandardResponse: A standard response indicating the status of the operation.
        """
        score: Score = next(
            (score for score in self.__scores
             if score.municipality_id == entity.municipality_id and score.period == entity.period),
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


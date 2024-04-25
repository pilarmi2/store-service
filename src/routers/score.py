from typing import Annotated

from fastapi import Body

from src.models.score import router
from src.models.score import Score
from src.models.standard_response import StandardResponse
from src.repository.repository import Repository
from src.repository.score_repository import ScoreRepository

repository: Repository = ScoreRepository()


@router.get('')
async def search_score(
        municipality_id: str,
        period: str
):
    return repository.get_by_id_and_period(municipality_id, period)


@router.post("")
async def create_score(
        municipality_id: str,
        score: Annotated[Score, Body()]
) -> StandardResponse:
    if municipality_id != score.municipality_id:
        return StandardResponse(status="400", message="Wrong municipality_id")
    return repository.add_or_update(score)

from typing import Annotated

from fastapi import Body

from src.models.score import router
from src.models.score import Score
from src.models.standard_response import StandardResponse


@router.get('')
async def search_score(
        id: int,
        period: str
):
    return {"id": id,
            "score": 464.616,
            "period": period}


@router.post("")
async def create_loans_statement(
        loans_statement: Annotated[Score, Body()],
) -> StandardResponse:
    return StandardResponse(status=201, message="Created")

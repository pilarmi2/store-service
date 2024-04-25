from typing import Annotated, Optional, List

from fastapi import Body

from src.models.municipality import router, Municipality
from src.models.standard_response import StandardResponse
from src.repository.municipality_repository import MunicipalityRepository
from src.repository.repository import Repository

repository: Repository = MunicipalityRepository()


@router.get("")
async def search_municipality() -> List[Municipality]:
    return repository.get_all()


@router.get("/{municipality_id}")
async def search_municipality_by_id(
        municipality_id: str
) -> Optional[Municipality]:
    return repository.get_by_id(municipality_id)


@router.post("")
async def create_municipality(
        municipality: Annotated[Municipality, Body()]
) -> StandardResponse:
    return repository.add_or_update(municipality)

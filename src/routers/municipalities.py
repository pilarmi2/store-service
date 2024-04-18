from typing import Annotated, Union, Optional

from fastapi import Query, Header, Body

from src.models.municipalities import GetMunicipalitiesResponseWrapper, router, Municipality, StandardResponse


@router.get("")
async def search_municipality(
    id: Annotated[list[int], Query()] = None,
    name: Annotated[list[str], Query()] = None
) -> GetMunicipalitiesResponseWrapper:
    return GetMunicipalitiesResponseWrapper(
        municipalities=[]
    )

@router.get("/{id}")
async def search_municipality_by_id(
    id: int
) -> Optional[Municipality]:
    return {"id": id, "name": "Praha", "citizens": 1156658}

@router.post("")
async def create_municipality(
    municipality: Annotated[Municipality, Body()],
    correlation_id: Annotated[Union[str, None], Header()] = None,
) -> StandardResponse:
    return StandardResponse(status=201, message="Created")
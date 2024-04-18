from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/municipalities",
    tags=["Municipalities"],
)


class Municipality(BaseModel):
    id: int
    name: str
    citizens: int = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class GetMunicipalitiesResponseWrapper(BaseModel):
    municipalities: list[Municipality]

class StandardResponse(BaseModel):
    status: int
    message: str


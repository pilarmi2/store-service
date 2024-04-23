from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/municipalities",
    tags=["Municipalities"],
)


class Municipality(BaseModel):
    municipality_id: int
    name: str
    citizens: int = None
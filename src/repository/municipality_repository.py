from typing import List

from src.models.municipalities import Municipality
from src.repository.repository import Repository
from src.models.standard_response import StandardResponse


class MunicipalityRepository(Repository):
    def __init__(self):
        self.__municipalities: List[Municipality] = []

    def get_all(self) -> List[Municipality]:
        return self.__municipalities

    def get_by_id(self, object_id: int) -> Municipality:
        return next(
            (municipality for municipality in self.__municipalities if municipality.municipality_id == object_id),
            None
        )

    def get_by_id_and_period(self, object_id: int, period: str):
        pass

    def add_or_update(self, entity: Municipality):
        municipality: Municipality = next(
            (municipality for municipality in self.__municipalities if municipality.municipality_id == entity.municipality_id),
            None
        )

        if municipality is None:
            self.__municipalities.append(entity)
            return StandardResponse(status=200, message="Created")
        else:
            municipality.municipality_id = entity.municipality_id
            municipality.name = entity.name
            municipality.citizens = entity.citizens
            return StandardResponse(status=200, message=f"Municipality with id {municipality.municipality_id} updated")


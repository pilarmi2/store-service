from typing import List

from src.models.municipality import Municipality
from src.repository.repository import Repository
from src.models.standard_response import StandardResponse


class MunicipalityRepository(Repository):
    """
    Represents a repository for managing municipalities.

    This repository allows for retrieving, adding, and updating municipalities.

    Attributes:
        __municipalities (List[Municipality]): A list to store municipalities.

    Methods:
        get_all() -> List[Municipality]: Retrieves all municipalities.
        get_by_id(object_id: str) -> Municipality: Retrieves a municipality by its ID.
        add_or_update(entity: Municipality): Adds or updates a municipality.
    """

    def __init__(self):
        self.__municipalities: List[Municipality] = []

    def get_all(self) -> List[Municipality]:
        """
        Retrieves all municipalities.

        Returns:
            List[Municipality]: A list of all municipalities.
        """
        return self.__municipalities

    def get_by_id(self, object_id: str) -> Municipality:
        """
        Retrieves a municipality by its ID.

        Args:
            object_id (str): The ID of the municipality to retrieve.

        Returns:
            Municipality: The municipality with the specified ID, if found; otherwise, None.
        """
        return next(
            (m for m in self.__municipalities if m.municipality_id == object_id),
            None
        )

    def get_by_id_and_period(self, object_id: str, period: str):
        pass  # This method must be implemented due to the abstract class Repository, but is not used.

    def add_or_update(self, entity: Municipality) -> StandardResponse:
        """
        Adds or updates a municipality.

        If a municipality with the same ID already exists, it updates the existing municipality.
        Otherwise, it adds the new municipality to the repository.

        Args:
            entity (Municipality): The municipality to add or update.

        Returns:
            StandardResponse: A standard response indicating the status of the operation.
        """
        municipality: Municipality = next(
            (m for m in self.__municipalities if m.municipality_id == entity.municipality_id),
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

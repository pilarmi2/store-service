from abc import ABC, abstractmethod


class Repository(ABC):
    """
    Abstract base class for repositories, defining the interface
    for working with data.

    Implementations of repositories must provide methods for:
    - retrieving all items
    - retrieving an item by ID
    - retrieving an item by ID and period
    - adding or updating an item.

    This class inherits from ABC (Abstract Base Class) from the abc module
    and contains abstract methods that must be implemented by subclasses.
    """

    @abstractmethod
    def get_all(self):
        """
        Abstract method to retrieve all items from the repository.
        """
        pass

    @abstractmethod
    def get_by_id(self, object_id: str):
        """
        Abstract method to retrieve an item from the repository by its ID.

        Args:
            object_id (str): The ID of the object to retrieve.

        Returns:
            object: The object corresponding to the given ID.
        """
        pass

    @abstractmethod
    def get_by_id_and_period(self, object_id: str, period: str):
        """
        Abstract method to retrieve an item from the repository by its ID and period.

        Args:
            object_id (str): The ID of the object to retrieve.
            period (str): The period for which the object should be retrieved.

        Returns:
            object: The object corresponding to the given ID and period.
        """
        pass

    @abstractmethod
    def add_or_update(self, entity: object):
        """
        Abstract method to add or update an item in the repository.

        Args:
            entity (object): The object to add or update in the repository.
        """
        pass

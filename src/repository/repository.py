from abc import ABC, abstractmethod


class Repository(ABC):
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, object_id: int):
        pass

    @abstractmethod
    def get_by_id_and_period(self, object_id: int, period: str):
        pass

    @abstractmethod
    def add_or_update(self, entity: object):
        pass

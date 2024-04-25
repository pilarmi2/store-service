import unittest

from src.models.municipality import Municipality
from src.repository.municipality_repository import MunicipalityRepository
from src.repository.repository import Repository


class MunicipalityRepositoryTest(unittest.TestCase):
    def test_add_municipality(self):
        repository: Repository = MunicipalityRepository()
        assert repository.get_all() == []
        repository.add_or_update(Municipality(municipality_id="1", name="Sample Municipality", citizens=1000))
        assert repository.get_all() != []
        assert repository.get_by_id("1").name == "Sample Municipality"

    def test_update_municipality(self):
        repository: Repository = MunicipalityRepository()
        repository.add_or_update(Municipality(municipality_id="1", name="Sample Municipality", citizens=1000))
        assert repository.get_by_id("1").name == "Sample Municipality"
        repository.add_or_update(Municipality(municipality_id="1", name="Prague", citizens=1000))
        assert repository.get_by_id("1").name == "Prague"

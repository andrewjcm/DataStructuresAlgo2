from abc import ABC, abstractmethod

from csv_interface.csv_reader import read_packages_csv
from model.map import create_map
from model.hashtable import HashTable


class Strategy(ABC):
    """
    Abstract base class for strategy.
    """

    map = create_map()
    packages = read_packages_csv()
    total_distance: float
    hash_table: HashTable = HashTable(len(packages))

    @abstractmethod
    def execute(self):
        pass

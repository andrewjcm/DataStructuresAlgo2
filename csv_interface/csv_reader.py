import csv
from typing import List


def read_packages_csv(dir: str = "csv_interface/csv_data/packages.csv") -> List[dict]:
    """
    Reads the packages from csv file and creates a list of dictionaries.

    Space-Time: O(n)

    :param dir: directory string to the file
    :return: list of all packages containing a dictionary of package details
    """
    contents = []
    with open(dir, newline='', encoding='utf-8-sig') as csv_file:
        file_contents = csv.DictReader(csv_file)
        for f in file_contents:
            contents.append(f)
    return contents


def read_addresses(dir: str = "csv_interface/csv_data/addresses.csv") -> dict:
    """
    Reads the addresses from csv file and creates a dictionary.

    Space-Time: O(n)

    :param dir: directory string to the file
    :return: dictionary with the address as the key and the corresponding index
    """
    addr_dict = {}
    with open(dir, encoding="utf-8-sig") as csv_file:
        file_contents = csv.reader(csv_file)
        for f in file_contents:
            addr_dict[f[0]] = int(f[1])
    return addr_dict


def read_distance_table(dir: str = "csv_interface/csv_data/distances.csv") -> List[list]:
    """
    Reads the distances from csv file and creates a matrix (list of lists).

    Space-Time: O(n)

    :param dir: directory string to the file
    :return: distance matrix
    """
    addresses: List[List[float]] = []
    with open(dir, encoding='utf-8-sig') as csv_file:
        file_contents = csv.reader(csv_file)
        for f in file_contents:
            addresses.append([float(i) for i in f if i != ""])
    return addresses


if __name__ == "__main__":
    print(read_distance_table())



import csv
from typing import List


def read_packages_csv(dir=""):
    contents = []
    with open(f"{dir}csv_interface/csv_data/packages.csv", newline='', encoding='utf-8-sig') as csv_file:
        file_contents = csv.DictReader(csv_file)
        for f in file_contents:
            contents.append(f)
    return contents


def read_addresses(dir=""):
    addr_dict = {}
    with open(f"{dir}csv_interface/csv_data/addresses.csv", encoding="utf-8-sig") as csv_file:
        file_contents = csv.reader(csv_file)
        for f in file_contents:
            addr_dict[f[0]] = int(f[1])
    return addr_dict


def read_distance_table(dir=""):
    addresses: List[List[float]] = []
    with open(f"{dir}csv_interface/csv_data/distances.csv", encoding='utf-8-sig') as csv_file:
        file_contents = csv.reader(csv_file)
        for f in file_contents:
            addresses.append([float(i) for i in f if i != ""])
    return addresses


if __name__ == "__main__":
    print(read_distance_table())



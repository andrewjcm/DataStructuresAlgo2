from __future__ import annotations
from typing import List
from csv_interface.csv_reader import read_addresses, read_distance_table


class Address:
    def __init__(self, name: str) -> None:
        """
        Address implementation of vertices of a graph.

        Space-Time: O(1)

        :param name: street name
        """
        self.name = name

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def equals(self, other: Address) -> bool:
        """
        Checks if one address is equal to another.

            __eq__ not used due to the Address objects being used
            as dictionary keys.

        Space-Time: O(1)

        :param other: another Address object
        :return: True or False
        """
        if isinstance(other, Address):
            return self.name == self.name


class Edge:
    def __init__(self, address1: Address, address2: Address, weight: float) -> None:
        """
        Creates edge between one address and another and holds the distance.

        Space-Time: O(1)

        :param address1: first connected address
        :param address2: second connected address
        :param weight: distance between the two addresses
        """
        self.address1 = str(address1)
        self.address2 = str(address2)
        self.weight = weight

    def __repr__(self):
        return f"Edge: {self.address1} <----({self.weight})----> {self.address2}"


class Path:
    def __init__(self, from_address: Address, to_address: Address, subset: List[Address], total_cost: float) -> None:
        """
        Creates a path object that stores the distance between two addresses with a subset of address between
        the first and last point.

        Space-Time: O(1)

        :param from_address: first address
        :param to_address: last address
        :param subset: list of addresses between
        :param total_cost: total distance to pass through all addresses between the first and last
        """
        self.from_address = str(from_address)
        self.to_address = str(to_address)
        self.subset = subset
        self.total_cost = total_cost

    def __repr__(self):
        return f"{self.from_address} to {self.to_address}"

    def equals(self, other: Path) -> bool:
        """
        Checks if one path is equal to another - regardless if the path is reversed.

        Space-Time: O(n)

        :param other: another Path object
        :return: True or False
        """
        if isinstance(other, Path):
            return (self.from_address == other.from_address and self.to_address == other.to_address
                    and self.subset == other.subset) \
                   or (self.from_address == other.to_address and self.to_address == other.from_address
                       and self.subset == reversed(other.subset))

    def __gt__(self, other):
        if isinstance(other, Path):
            return self.total_cost > other.total_cost

    def __lt__(self, other):
        if isinstance(other, Path):
            return self.total_cost < other.total_cost


class Map:
    def __init__(self) -> None:
        """
        Implementation of a graph as a map connecting all addresses together and their distances.

        Space-Time: O(n)
        """
        self.vertices = dict()

    def add_edge(self, edge: Edge) -> None:
        """
        Adds an edge object into the graph and updates address adjacency's.

        :param edge: an Edge object
        :return: None
        """
        if edge.address1 not in self.vertices:
            self.vertices[edge.address1] = dict()

        if edge.address1 not in self.vertices:
            self.vertices[edge.address2] = dict()

        # Adjacency
        self.vertices[edge.address1][edge.address2] = edge.weight
        self.vertices[edge.address2][edge.address1] = edge.weight

    def print_graph(self) -> None:
        """
        Prints the graph.

        Space-Time: O(n)

        :return: None
        """
        for key in self.vertices:
            print(f"{key} {len(self.vertices[key])}-> {self.vertices[key]}")


def create_map() -> Map:
    """
    Creates a full map of all addresses and distances from the csv data.

    Space-Time: O(n^2)

    :return: a full map of all addresses
    """
    addrs = read_addresses()
    dist = read_distance_table()

    map = Map()

    addr_list = []
    for addr in addrs:
        addr_list.append(Address(addr))

    for c1, i in enumerate(dist):
        for c2, j in enumerate(i):
            edge = Edge(addr_list[c1], addr_list[c2], float(j))
            map.add_edge(edge)

    return map

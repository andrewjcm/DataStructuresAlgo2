from csv_interface.csv_reader import read_addresses, read_distance_table


class Address:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def equals(self, other):
        if isinstance(other, Address):
            return self.name == self.name


class Edge:
    def __init__(self, vertex1, vertex2, weight):
        self.vertex1 = str(vertex1)
        self.vertex2 = str(vertex2)
        self.weight = weight

    def __repr__(self):
        return f"Edge: {self.vertex1} <----({self.weight})----> {self.vertex2}"


class Path:
    def __init__(self, from_vertex, to_vertex, subset, total_cost):
        self.from_vertex = str(from_vertex)
        self.to_vertex = str(to_vertex)
        self.subset = subset
        self.total_cost = total_cost

    def __repr__(self):
        return f"{self.from_vertex} to {self.to_vertex}"

    def equals(self, other):
        if isinstance(other, Path):
            return (self.from_vertex == other.from_vertex and self.to_vertex == other.to_vertex) \
                   or (self.from_vertex == other.to_vertex and self.to_vertex == other.from_vertex)

    def __gt__(self, other):
        if isinstance(other, Path):
            return self.total_cost > other.total_cost

    def __lt__(self, other):
        if isinstance(other, Path):
            return self.total_cost < other.total_cost


class Map:
    def __init__(self):
        self.vertices = dict()

    def add_edge(self, edge):
        if edge.vertex1 not in self.vertices:
            self.vertices[edge.vertex1] = dict()

        if edge.vertex1 not in self.vertices:
            self.vertices[edge.vertex2] = dict()

        # Adjacency
        self.vertices[edge.vertex1][edge.vertex2] = edge.weight
        self.vertices[edge.vertex2][edge.vertex1] = edge.weight

    def print_graph(self):
        for key in self.vertices:
            print(f"{key} {len(self.vertices[key])}-> {self.vertices[key]}")


def create_map():
    addrs = read_addresses("")
    dist = read_distance_table("")

    map = Map()

    addr_list = []
    for addr in addrs:
        addr_list.append(Address(addr))

    for c1, i in enumerate(dist):
        for c2, j in enumerate(i):
            edge = Edge(addr_list[c1], addr_list[c2], float(j))
            map.add_edge(edge)

    return map

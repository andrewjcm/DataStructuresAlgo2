from typing import List

from model.package import Package
from model.truck import Truck
from strategy.strategy import Strategy


class NearestNeighbor(Strategy):
    """A Strategy class to Implement the Nearest Neighbor algorithm."""

    def nearest_neighbor_algo(self, current_addr: str, remaining_packages: List[Package]) -> dict:

        """
        This method uses the nearest neighbor algorithm to determine the next package to deliver.

        Space-Time: O(n)

        :param current_addr: the starting address
        :param remaining_packages: the remaining packages to be delivered
        :return: returns the next closest package to be delivered and the distance from the current address
        """
        # Get all the distances
        distance_set = {
            next_pack: self.map.vertices[current_addr][next_pack.address] for next_pack in remaining_packages
        }

        # Min distance
        next_package = min(distance_set, key=lambda k: distance_set[k])

        return {
            "nearest_neighbor": next_package,
            "distance": distance_set[next_package]
        }

    @property
    def create_package_objects(self) -> List[Package]:
        """
        Creates a list of Package objects from the imported data.

        Space-Time: O(n)

        :return: Package objects
        """
        return [Package(**package) for package in self.packages]

    def fill_hash_table(self) -> None:
        """
        Fills the hash table with packages.

        Space-Time: O(n)

        :return: None
        """
        for package in self.create_package_objects:
            self.hash_table.insert(package.id, package)

    def deliver_packages(self, truck: Truck) -> None:
        """
        Loops through a truck load and delivers packages until load is empty.

        Space-Time: O(n^2)

        :param truck: a Truck object.
        :return: None
        """
        while truck.packages_loaded > 0:
            route = truck.priority_route if len(truck.priority_route) > 0 else truck.route
            nearest_neighbor = self.nearest_neighbor_algo(truck.current_loc, route)
            truck.space_time(nearest_neighbor["distance"])
            truck.deliver_package(nearest_neighbor["nearest_neighbor"])

    def execute(self) -> None:
        """"
        Executes the Nearest Neighbor algorithm.

        Space-Time: O(n^2)
        """
        # Fill Hash Table
        self.fill_hash_table()

        # Create Trucks
        t1 = Truck(1, self.hash_table)
        t2 = Truck(2, self.hash_table, "9:05")

        # Manually load the trucks
        load_one = [39, 13, 14, 15, 16, 20, 29, 30, 23, 34, 37, 40, 4, 8, 7, 5]
        load_two = [1, 31, 3, 6, 18, 25, 28, 32, 36, 38, 19, 21, 10, 27, 26, 22]
        load_three = [9, 12, 24, 11, 33, 2, 35, 17]

        t1.load_truck(load_one)

        t2.load_truck(load_two)

        # First Truck Deliveries
        self.deliver_packages(t1)

        # Second Truck Deliveries
        self.deliver_packages(t2)

        # Check which truck is closest to the hub and assign it to final_truck
        final_truck = t1 if self.map.vertices[t1.current_loc]["HUB"] < self.map.vertices[t2.current_loc]["HUB"] else t2

        # Update wrong address
        wrong_addr_package = self.hash_table.get(9)
        wrong_addr_package.address = "410 S State St"
        wrong_addr_package.zip_code = "84111"

        # Go to the hub
        final_truck.return_to_hub(self.map.vertices[final_truck.current_loc]["HUB"])

        # Load final truck
        final_truck.load_truck(load_three)

        # Final Truck Deliveries
        self.deliver_packages(final_truck)

        # Set total distance traveled
        self.total_distance = round(t1.distance_traveled + t2.distance_traveled, 2)


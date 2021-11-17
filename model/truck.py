from datetime import datetime, timedelta
from typing import List

from model.hashtable import HashTable
from model.package import Package


class Truck:
    def __init__(self, id: int, hash_table: HashTable, current_time: str = "8:00") -> None:
        """
        Instantiate a Truck object.

        Space-Time: O(1)

        :param id: truck id
        :param hash_table: package hash table
        :param current_time: start time of the truck
        """
        self.id = id
        self.packages_loaded = 0
        self.max_packages = 16
        self.mph = 18
        self.priority_route = []
        self.route = []
        self.current_loc = "HUB"
        self.distance_traveled = 0
        self.current_time = datetime.strptime(current_time, "%H:%M")
        self.package_hash = hash_table

    # O(1)
    def add_package(self, package: Package, ordered: bool = False) -> None:
        """
        Adds and individual package object to the truck.

        Space-Time: O(1)

        :param package: selected package to be added to to the truck
        :param ordered: True if the order load was already optimized. Default is False
        :return: None
        """
        if package.notes == "Can only be on truck 2" and self.id != 2:
            raise Exception(f"Package {package.id} can only be loaded onto truck 2.")
        if self.packages_loaded < self.max_packages:
            package.status = "In route"
            if not ordered:
                if package.priority:
                    self.priority_route.append(package)
                else:
                    self.route.append(package)
            else:
                self.route.append(package)
            self.packages_loaded += 1

        else:
            raise Exception("Truck is full.")

    def load_truck(self, package_ids: List[int], ordered: bool = False) -> None:
        """
        Takes a list of package ids, queries the hash table to retrieve the package
        object and loads the truck.

        Space-Time: O(n)

        :param package_ids: List of package ids
        :param ordered: True if the load order has already been optimized. Default is False
        :return:
        """
        for i in package_ids:
            self.add_package(self.package_hash.get(i), ordered)

    def deliver_package(self, package: Package) -> None:
        """
        Delivers the current package by:
            -Checking that it hasn't already been delivered. If it has it will
            throw and exception
            -Checking that it is on the truck. If isn't it will throw and exception

            -Updating the delivery time
            -Updating the deliver status
            -Removing the package from the truck load
            -Decrements the package load count
            -Updates the trucks current location

        Space-Time: O(1)

        :param package: selected package to deliver
        :return: None
        """
        if package.status[:9] == "Delivered":
            raise Exception(f"Package ({package.id}) has already been delivered.")
        try:
            package.time_delivered = self.current_time
            self.update_delivery_status(package)
            if self.priority_route and package.priority:
                self.priority_route.remove(package)
            else:
                self.route.remove(package)
            self.packages_loaded -= 1
            self.current_loc = package.address
        except AttributeError:
            # Exception
            print("Package not on truck.")

    def return_to_hub(self, distance: float) -> None:
        """
        Returns the truck to the hub. Sets current location to the hub
        and updates the total distance and time.

        Space-Time: O(1)

        :param distance: distance from current location to the hub
        :return: None
        """
        self.current_loc = "HUB"
        self.space_time(distance)

    def space_time(self, distance: float) -> None:
        """
        Updates the trucks total distance and the current time.

        Space-Time: O(1)

        :param distance: distance between current location and next
        :return: None
        """
        self.distance_traveled += distance
        self.current_time += timedelta(hours=distance / self.mph)

    def update_delivery_status(self, package: Package) -> None:
        """
        Updates the delivery status of the selected package.

        Space-Time: O(1)

        :param package: package to update
        :return: None
        """
        try:
            deadline = datetime.strptime(package.deadline, "%I:%M %p")
            if deadline > package.time_delivered:
                package.status = f"Delivered on time at {package.time_delivered.time()}"
            else:
                package.status = f"Delivered LATE at {package.time_delivered.time()}"
        except ValueError:
            package.status = f"Delivered on time at {package.time_delivered.time()}"

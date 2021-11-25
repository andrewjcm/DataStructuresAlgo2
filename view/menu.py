from datetime import datetime
from typing import List

from model.package import Package


def get_menu_selection() -> int:
    """
    Prints main menu and gets the user's menu selection.

    Space-Time: O(n)

    :return: menu selection
    """
    print(f"\nMain Menu"
          f"\n(1) Show package status"
          f"\n(2) Show all package status"
          f"\n(3) Show total truck mileage"
          f"\n(0) Exit")
    selection = input("Selection: ")
    try:
        return int(selection)
    except ValueError:
        print_invalid_selection()
        return get_menu_selection()


def get_selected_package_id() -> int:
    """
    Prints the request for package id and gets package id.

    Space-Time: O(n)

    :return: user input
    """
    package_id = input("Enter package id: ")
    try:
        return int(package_id)
    except ValueError:
        return get_selected_package_id()


def get_selected_time() -> datetime.time:
    """
    Prints request for time and gets the time entered.

    Space-Time: O(n)

    :return: user input
    """
    time = input("Enter time (HH:MM or leave blank): ")
    try:
        return datetime.strptime(time, "%H:%M").time()
    except ValueError:
        if time == "":
            return None
        else:
            print("Invalid entry.")
            return get_selected_time()


def print_package_status(package: Package, time: datetime.time = None) -> None:
    """
    Prints the specified Package object. Based on time param, the package status
    will be updated.

    Space-Time: O(1)

    :param package: selected Package object
    :param time: specified time by the user
    :return: None
    """
    if time:
        if package.id == 9:
            addr_update = datetime.strptime("10:20", "%H:%M").time()
            package.address = "300 State St" if time < addr_update else "410 S State St"
            package.zip_code = "84103" if time < addr_update else "84111"
        if package.time_delivered.time() > time:
            package.status = "In transit"
        else:
            package.status = f"Delivered at {package.time_delivered.time()}"
    else:
        package.status = f"Delivered at {package.time_delivered.time()}"

    print(package)


def print_all_packages(package_list: List[Package], time: datetime.time = None) -> None:
    """
    Prints all Package objects. Based on time param, the package status will be updated.

    Space-Time: O(n)

    :param package_list: list of all Package objects
    :param time: specified time by the user
    :return: None
    """
    for package in package_list:
        print_package_status(package, time)


def print_total_mileage(mileage: float) -> None:
    """
    Prints the total mileage required to deliver all packages.

    Space-Time: O(1)

    :param mileage: total mileage to print
    :return: None
    """
    print(f"Total mileage: {mileage}")


def print_exiting() -> None:
    """
    Informs the user that the program is exiting.

    Space-Time: O(1)

    :return: None
    """
    print("Exiting...")


def print_invalid_selection() -> None:
    """
    Informs the user of an invalid selection.

    Space-Time: O(1)

    :return: None
    """
    print("Sorry, Buckaroonie! That's not on the menu.")


from datetime import datetime


def get_menu_selection():
    print(f"\nMain Menu"
          f"\n(1) Show package status"
          f"\n(2) Show all package status"
          f"\n(3) Show total truck mileage"
          f"\n(0) Exit")
    selection = input("Selection: ")
    try:
        return int(selection)
    except ValueError:
        return get_menu_selection()


def get_selected_package_id():
    package_id = input("Enter package id: ")
    try:
        return int(package_id)
    except ValueError:
        return get_selected_package_id()


def get_selected_time():
    time = input("Enter time (HH:MM or leave blank): ")
    try:
        return datetime.strptime(time, "%H:%M").time()
    except ValueError:
        if time == "":
            return None
        else:
            print("Invalid entry.")
            return get_selected_time()


def print_package_status(package, time=None):
    if time:
        if package.time_delivered.time() > time:
            package.status = "In transit"
    print(package)


def print_all_packages(package_list, time=None):
    for package in package_list:
        print_package_status(package, time)


def print_total_mileage(mileage):
    print(f"Total mileage: {mileage}")


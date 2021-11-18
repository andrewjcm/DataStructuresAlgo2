from strategy.nearest_neighbor import NearestNeighbor
from view.menu import *


class MenuController:
    """Controller for the menu view."""
    def __init__(self):
        self.menu_item = -1

    def show(self) -> None:
        """
        Shows the menu view and runs the set strategy.

        Time-Space: O(n^3)

        :return: None
        """
        # Run the strategy
        strat = NearestNeighbor()
        strat.execute()

        # Show the menu
        while self.menu_item != 0:

            self.menu_item = get_menu_selection()

            if self.menu_item == 1:
                package = strat.hash_table.get(get_selected_package_id())
                time = get_selected_time()
                print_package_status(package, time)
            elif self.menu_item == 2:
                time = get_selected_time()
                for i in range(len(strat.hash_table.table)):
                    print_package_status(strat.hash_table.get(i + 1), time)
            elif self.menu_item == 3:
                print_total_mileage(strat.total_distance)
            elif self.menu_item == 0:
                print_exiting()
            else:
                print_invalid_selection()

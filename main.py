# Author: Andrew Cesar-Metzgus 007646579
from controller.menu import MenuController


def main() -> None:
    """
    Main method to run entire program from the menu controller.

    Space-Time:

    :return: None
    """
    menu = MenuController()
    menu.show()


if __name__ == "__main__":
    main()

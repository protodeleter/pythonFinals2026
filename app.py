from importlib.metadata import requires

from cargo_item import CargoItem
from cargo_station import CargoStation
from db import Db
from special_cargo import SpecialCargo
from validator import Validator


class App:
    def __init__(self, cargo_station):
        self._cs = cargo_station

    def _cut_the_process(self, value):
        if value == "**":
            return False
        return None

    def add_cargo(self):

        danger_level = None
        requires_cooling = None
        speacial_cargo_flag = False

        is_special_cargo = input("Is it special cargo? (Y/N) ")
        if is_special_cargo == "Y":
            speacial_cargo_flag = True


        cname = input("Enter Cargo Name: (Enter ** to exit)")
        if self._cut_the_process(cname):
            return False

        while cname == "" or not Validator.minimum_length(cname, 2):
            cname = input("Enter Cargo Name: (Enter ** to exit)")
            if self._cut_the_process(cname):
                return False

        cweight = input("Enter Cargo Weight: (Enter ** to exit)")
        if self._cut_the_process(cweight):
            return False

        while cweight == "" or not Validator.validate_positive_numbers(cweight) and not cweight == "**":
            print("Cargo weight must be a positive number. (Enter ** to exit)")
            cweight = input("Enter Cargo Weight: ")
            if self._cut_the_process(cweight):
                return False

        cweight = float(cweight)

        cplanet = input("Enter Cargo Planet: (Enter ** to exit)")
        if self._cut_the_process(cplanet):
            return False
        while not Validator.minimum_length(cplanet, 1) and not cplanet == "**":
            cplanet = input("Cargo Planet cannot be empty: (Enter ** to exit)")
            if self._cut_the_process(cplanet):
                return False

        if speacial_cargo_flag:

            while True:
                try:
                    inp = input("Enter Cargo Danger Lever: (Enter ** to exit)")
                    if inp == "**":
                        self._cut_the_process(cplanet)
                        return False

                    inp = int(inp)
                    if inp < 1 or inp > 5:
                        print("Cargo Danger Lever must be between 1 and 5")
                        break
                    danger_level= inp

                except ValueError:
                    print("Please enter numbers only")

            while True:

                try:
                    inp = input("Is cargo requires cooling: (Enter ** to exit) \n possible values 1 | 0 \n")
                    if inp == "**":
                        self._cut_the_process(cplanet)
                        return False
                    inp = int(inp)
                    requires_cooling = inp
                except ValueError:
                    print("Please enter numbers only")

                ci = SpecialCargo(cname, cweight, cplanet,danger_level,requires_cooling )
                self._cs.add_item(ci)

        else:
            ci = CargoItem(cname, cweight, cplanet)
            self._cs.add_item(ci)

        return None

    def remove_cargo(self):

        items = self._cs.get_all_items()
        print(self._cs.get_all_items())

        if not items:
            print("Cargo Item Not Found")
            return

        while True:
            try:
                itm = input("Enter item id: (type ** to main menu) ")
                if itm == "**":
                    self._main_menu()
                    return False
                itm = int(itm)
                self._cs.remove_item(itm)

            except ValueError:
                print("Please enter numbers only")

    def find_cargo(self):
        print("*** Find Cargo Item ***")

        while True:
            try:
                itm = input("Enter item id: (type ** to main menu) ")
                if itm == "**":
                    self._main_menu()
                    return None
                itm = int(itm)

                if self._cs.find_item_by_id(itm):
                    print("Cargo Item Found")
                    print(self._cs.find_item_by_id(itm))
                else:
                    print("Cargo Item Not Found")

            except ValueError:
                print("Please enter numbers only")

    def show_total_weight(self):
        print("Show Total Weight")

    def show_all_items(self):
        for item in self._cs.get_all_items():
            print(item)


    def _main_menu(self):
        while True:

            cs = CargoStation()
            items = cs.get_all_items()
            main_menu = "1: Add cargo item \n"
            if items:
                main_menu += "2: Remove cargo item\n"
            if items:
                main_menu += "3: Find cargo item\n"
            if items:
                main_menu += "4: Show total weight\n"
            if items:
                main_menu += "5: Show all items \n"
            main_menu += "6: Exit"
            try:
                option = int(input(
                    'Choose an option: \n' + main_menu))
                option = int(option)
                if option == 1:
                    self.add_cargo()
                if option == 2 and items:
                    self.remove_cargo()
                if option == 3 and items:
                    self.find_cargo()
                if option == 4 and items:
                    self.show_total_weight()
                if option == 5 and items:
                    self.show_all_items()
                if option == 6 and items:
                    return
                if option > 6:
                    exit(0)
            except ValueError:
                print("Please enter numbers only")

    def run(self):
        self._main_menu()

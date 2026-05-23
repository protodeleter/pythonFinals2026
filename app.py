from importlib.metadata import requires

from CargoNotFoundError import CargoNotFoundError
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

        speacial_cargo_flag = False

        is_special_cargo = input("Is it special cargo? (Y) ")


        if is_special_cargo == "Y" or is_special_cargo == "y" :
            speacial_cargo_flag = True


        cname = input("Enter Cargo Name: (Enter ** to exit)")
        if self._cut_the_process(cname):
            return False

        while cname == "" or not Validator.minimum_length(cname, 2):
            cname = input("Enter Cargo Name: (Enter ** to exit)")
            if self._cut_the_process(cname):
                return False

        # cweight = input("Enter Cargo Weight: (Enter ** to exit)")
        # if self._cut_the_process(cweight):
        #     return False

        cweight = self._cs.get_cargo_weight()

        if not cweight:
            return False




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
                    inp = input("Enter Cargo Danger Level: (Enter ** to exit) ")

                    if inp == "**":
                        self._cut_the_process(cplanet)
                        return False

                    inp = int(inp)

                    if inp < 1 or inp > 5:
                        print("Cargo Danger Level must be between 1 and 5")
                    else:
                        danger_level = inp
                        break

                except ValueError:
                    print("Please enter numbers only")

            while True:
                try:
                    inp = input("Is cargo requires cooling: (Enter ** to exit) \n possible values 1 | 0 \n")
                    if inp == "**":
                        self._cut_the_process(cplanet)
                        return False
                    inp = int(inp)
                    if inp not in (0, 1):
                        print("Cargo Requires cooling must be between 1 and 0")
                    else:
                        requires_cooling = inp
                        break

                except ValueError:
                    print("Please enter numbers only")

            ci = SpecialCargo(cname, cweight, cplanet,danger_level,requires_cooling )
            self._cs.add_item(ci)

        else:
            ci = CargoItem(cname, cweight, cplanet)
            self._cs.add_item(ci)

        return None

    def remove_cargo(self) -> bool:

        print("*** Remove Cargo Item ***")
        items = self._cs.get_all_items()
        print(self._cs.get_all_items())

        if not items:
            print("Cargo Item Not Found")
            return False

        while True:
            try:
                itm = input("Enter item id: (type ** to main menu) ")
                if itm == "**":
                    self._main_menu()
                    return False
                item_id = int(itm)
                self._cs.remove_item(item_id)
                return True
            except ValueError:
                print("Please enter numbers only")
            except CargoNotFoundError as e:
                print(e)
                return True


    def find_cargo(self):
        print("*** Find Cargo Item ***")
        while True:
            try:
                itm = input("Enter item id: (type ** to main menu) ")
                if itm == "**":
                    self._main_menu()
                    return None
                itm = int(itm)
                item = self._cs.find_item_by_id(itm)
                print(item)
                return True
            except ValueError:
                print("Please enter numbers only")

            except CargoNotFoundError as e:
                print("****")
                print(e)
                print("****")

                return False

    def show_total_weight(self) -> None:
        print("*** Show Total Weight ***")
        print(self._cs.get_total_weight())

    def show_all_items(self) -> None:
        print("**** All Items ***")
        for item in self._cs.get_all_items():
            print(item)


    def _main_menu(self) -> None:
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
                if option == 6:
                    exit(0)

            except ValueError:
                print("Please enter numbers only")

    def run(self):
        self._main_menu()

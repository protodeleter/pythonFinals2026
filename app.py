from importlib.metadata import requires

from CargoNotFoundError import CargoNotFoundError
from cargo_item import CargoItem
from cargo_station import CargoStation
from db import Db
from error_logger import ErrorLogger
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

        ErrorLogger.write_log( "info" , "Add cargo started" , __name__ )

        speacial_cargo_flag = False
        is_special_cargo = input("Is it special cargo? (Y) ")
        if is_special_cargo == "Y" or is_special_cargo == "y" :
            speacial_cargo_flag = True
            ErrorLogger.write_log("info", "Speacial cargo", __name__)

        cname = self._cs.get_cargo_name()
        if cname is None:
            return False
        ErrorLogger.write_log("info", "Cargo name " + cname, __name__)

        cweight = self._cs.get_cargo_weight()
        if cweight is None:
            return False
        ErrorLogger.write_log("info", "Cargo weight " + str(cweight), __name__)

        cplanet = self._cs.get_cargo_planet()
        if not cplanet:
            return False
        ErrorLogger.write_log("info", "Cargo planet " + cplanet, __name__)

        if speacial_cargo_flag:
            danger_level = self._cs.get_danger_level()
            if danger_level is None:
                return False
            ErrorLogger.write_log("info", "Cargo danger level " + str(danger_level), __name__)

            requires_cooling = self._cs.get_requires_cooling()
            if requires_cooling is None:
                return False
            ErrorLogger.write_log("info", "Cargo requires_cooling " + str(requires_cooling), __name__)

            ci = SpecialCargo(cname, cweight, cplanet,danger_level,requires_cooling )
        else:
            ci = CargoItem(cname, cweight, cplanet)

        self._cs.add_item(ci)
        self.show_all_items()

        return None

    def remove_cargo(self) -> bool:

        ErrorLogger.write_log("info", "Remove cargo started ", __name__)

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
            print( f"Item id: {item["itemid"]} | name: {item["cargo_name"]} | weight: {item["cargo_weight"]} | planet: {item["cargo_origin_planet"]} | danger_level: {item["danger_level"]} | requires_cooling: {item["requires_cooling"]} " )



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

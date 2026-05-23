import random

from CargoNotFoundError import CargoNotFoundError
from cargo_item import CargoItem
from db import Db
from error_logger import ErrorLogger
from special_cargo import SpecialCargo
from validator import Validator


class CargoStation:

    def __init__(self):
        self._db = Db()
        self._cargo_items = self._db.get_all_items()

    @property
    def cargo_items(self):
        return self._cargo_items

    @cargo_items.setter
    def cargo_items(self, cargo_items: list):
        self._cargo_items = cargo_items

    def add_item(self, item: CargoItem | SpecialCargo) -> None:
        db = Db()

        cargo_name = getattr(item, "cargo_name", None)
        weight = getattr(item, "cargo_weight", None)
        requires_cooling = getattr(item, "requires_cooling", None)
        danger_level = getattr(item, "danger_level", None)
        planet = getattr(item, "cargo_origin_planet", None)

        item_data = {
            "itemid": int(item.item_id),
            "cargo_name": cargo_name,
            "cargo_weight": weight,
            "cargo_origin_planet": planet,
            "requires_cooling" : requires_cooling,
            "danger_level" : danger_level
        }


        if db.insert_item(item_data):
            print("****Item Added****")
            ErrorLogger.write_log( "info",f"Cargo Station: Item {int(item.item_id)} was added" , __name__ )
        else:
            print("Something went wrong")

    def remove_item(self, itemid: int) -> None:
        item_to_delete = self.find_item_by_id(itemid)

        try:
            self._db.delete_item(item_to_delete)
            ErrorLogger.write_log( f"Item {item_to_delete.get("cargo_name")} was removed")

        except CargoNotFoundError:
            print("Item not found")




    def find_item_by_id(self, itemid: int) -> CargoItem | SpecialCargo:
        for ci in self.get_all_items():
            if ci.get("itemid") == itemid:
                return ci

        raise CargoNotFoundError("Item not found")


    def get_total_weight(self) -> float:
        return sum(ci.get("cargo_weight", 0) for ci in self.get_all_items())

    def get_all_items(self) -> list:
        return self._db.get_all_items()

    def _print_all_items(self):
        for item in self.get_all_items():
            print(item)


    def _cut_the_process(self, value):
        if value == "**":
            ErrorLogger.write_log("info", "Process stopped by user ", __name__)
            return True
        return None


    def get_cargo_planet(self) -> str | bool:

        while True:
            try:
                cplanet = input("Enter Cargo Planet: (Enter ** to exit)")
                if self._cut_the_process(cplanet):
                    return False
                if not Validator.minimum_length(cplanet, 1):
                    print("Cargo Planet must not be empty")
                    continue

                cplanet = cplanet.strip()
                break

            except ValueError:
                print("Cargo not found")

        return cplanet




    def get_cargo_name(self) -> None | str :
        while True:
            try:
                cname = input("Enter Cargo Name: (Enter ** to exit)")
                if self._cut_the_process(cname):
                    return None
                if cname == "" or not Validator.minimum_length(cname, 2):
                    print("Cargo Name must be at least 2 characters")
                    continue
                cname = cname.strip()
                break

            except CargoNotFoundError:
                print("Cargo not found")
        return cname


    def get_cargo_weight(self) -> float|None:
        cargo_weight = 0
        while True:
            try:
                cweight = input("Enter Cargo Weight: (Enter ** to exit) ").strip()

                if self._cut_the_process(cweight):
                    return None

                if not Validator.validate_positive_numbers(cweight):
                    print("Cargo weight must be positive numbers")
                    continue

                cargo_weight = float(cweight)
                break

            except ValueError:
                print("Please enter numbers only")
        return cargo_weight

    def get_danger_level(self) -> None | int:
        while True:
            try:
                danger_level = input("Enter Cargo Danger Level: (Enter ** to exit) ")
                if self._cut_the_process(danger_level):
                    return None
                danger_level = int(danger_level)
                if danger_level < 1 or danger_level > 5 :
                    print("Cargo Danger Level must be between 1 and 5")
                    continue

                danger_level = danger_level
                break

            except ValueError:
                print("Please enter numbers only")
        return danger_level

    def get_requires_cooling(self) -> None | int:

        while True:
            try:
                requires_cooling = input("Is cargo requires cooling: (Enter ** to exit) \n possible values 1 | 0 \n")
                if self._cut_the_process(requires_cooling):
                    return None

                requires_cooling = int(requires_cooling)
                if requires_cooling not in (0, 1):
                    print("Cargo Requires cooling must be between 1 and 0")
                    continue

                requires_cooling = requires_cooling
                break

            except ValueError:
                print("Please enter numbers only")

        return requires_cooling
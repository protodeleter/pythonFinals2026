import random

import exceptions
from CargoNotFoundError import CargoNotFoundError
from cargo_item import CargoItem
from db import Db
from error_logger import ErrorLogger
from special_cargo import SpecialCargo
import validator

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

    def add_item(self, item: CargoItem | SpecialCargo) -> dict | None:
        """
        triggers db method insert_item
        :param item:
        :return:
        """
        res = None
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
            "requires_cooling": requires_cooling,
            "danger_level": danger_level
        }

        try:
            res = db.insert_item(item_data)
            ErrorLogger.write_log("info", f"Cargo Station: Item {int(item.item_id)} was added", __name__)
        except exceptions.GeneralError:
            print("Something went wrong")

        return res

    def remove_item(self, itemid: int) -> dict | None:
        """
        triggers db method delete_item
        :param itemid:
        :return:
        """
        try:
            inp = int(itemid)
            item_to_delete = self._db.delete_item(inp)
            if item_to_delete:
                ErrorLogger.write_log("info", f'Item {item_to_delete.get("cargo_name")} was removed', __name__)
                return item_to_delete
        except ValueError:
            print("Please enter a valid item id")
        return None

    def find_item_by_id(self, itemid: int) -> CargoItem | SpecialCargo:
        """
        finds item in list of items by itemid
        :param itemid:
        :return: CargoItem | SpecialCargo
        """
        for ci in self.get_all_items():
            if ci.get("itemid") == itemid:
                return ci

        ErrorLogger.write_log("Error", f"Item {itemid} not found", __name__)
        raise exceptions.CargoNotFoundError(f"Item {itemid} not found")

    def get_total_weight(self) -> float:
        """

        :return: total weight of all items
        """
        return sum(ci.get("cargo_weight", 0) for ci in self.get_all_items())

    def get_all_items(self) -> list:
        """

        :return: list of all items
        """
        return self._db.get_all_items()

    def _print_all_items(self):
        """
        prints all items
        :return:
        """
        for item in self.get_all_items():
            print(item)

    def _cut_the_process(self, value) -> bool | None:
        """
        check if value is **
        :param value:
        :return: bool | None
        """
        if value == "**":
            ErrorLogger.write_log("info", "Process stopped by user ", __name__)
            return True
        return None

    def get_cargo_planet_input(self) -> str | None:
        """
        triggers get_cargo_planet and returns input
        :return: string
        """
        planet = ""
        while True:
            inp = input("Enter Cargo planet: (Enter ** to exit)")
            planet = self.get_cargo_planet(inp)
            if self._cut_the_process(inp):
                return None
            if not planet:
                print("Please enter corrent planet")
                continue
            else:
                planet = inp
                break
        return planet

    def get_cargo_name_input(self) -> None | str:
        """
        triggers get_cargo_name and returns input
        :return: string
        """
        cname = ""
        while True:
            inp = input("Enter Cargo Name: (Enter ** to exit)")
            if self._cut_the_process(inp):
                return None
            if not self.get_cargo_name(inp):
                print("Please enter corrent name ( longer then 2 charachters) ")
                continue
            else:
                cname = inp
                break
        return cname

    def get_cargo_weight_input(self) -> float | None:
        """
         triggers get_cargo_weight and returns input
         :return: float
         """
        while True:
            try:
                inp = input("Enter Cargo Weight: (Enter ** to exit) ").strip()
                if self._cut_the_process(inp):
                    return None
                cargo_weight = self.get_cargo_weight(inp)
                if cargo_weight is None:
                    print("Please enter positive numbers only")
                    continue
                return cargo_weight
            except exceptions.CargoWeightPositiveError:
                print("Please enter numbers only")

    def get_danger_level_inp(self) -> None | int:
        while True:
            try:
                danger_level = input("Enter Cargo Danger Level: (Enter ** to exit) ")
                if self._cut_the_process(danger_level):
                    return None

                danger_level = self.get_danger_level(danger_level)
                if danger_level is None:
                    print("Please enter numbers only between 1 and 5")
                    continue
                return danger_level
            except ValueError:
                print("Please enter numbers only")

    def get_requires_cooling_inp(self) -> None | int:
        while True:
            try:
                requires_cooling = input("Is cargo requires cooling: (Enter ** to exit) \n possible values 1 | 0 \n")
                if self._cut_the_process(requires_cooling):
                    return None
                requires_cooling = self.get_requires_cooling(requires_cooling)
                if requires_cooling is None:
                    print("Please enter numbers only between 1 and 0")
                    continue
                return requires_cooling
            except ValueError:
                print("Please enter numbers only")

    def get_cargo_name(self, cname: str) -> str | None:
        return validator.validate_name(cname)

    def get_cargo_weight(self, weight) -> float | None:
        return validator.validate_positive_numbers(weight)

    def get_cargo_planet(self, planet) -> str | None:
        return validator.validate_planet(planet)

    def get_danger_level(self, danger_level) -> int | None:
        return validator.validate_danger_level(danger_level)

    def get_requires_cooling(self, cooling) -> int | None:
        return validator.validate_cooling_level(cooling)

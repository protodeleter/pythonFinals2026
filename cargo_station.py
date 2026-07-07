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
        """
        initialize CargoStation
        load DB and cargo items
        :return:
        """
        self._db = Db()
        self.__cargo_items = self._db.get_all_items()

    @property
    def cargo_items(self):
        """
        getter for cargo_items
        :return: list
        """
        return self._cargo_items


    @cargo_items.setter
    def cargo_items(self, cargo_items: list):
        """
        setter for cargo_items
        :param cargo_items:
        :return:
        """
        self._cargo_items = cargo_items

    def add_item(self, item: CargoItem | SpecialCargo) -> dict | None:
        """
        triggers db method insert_item
        :param item:
        :return: inserted item dict or None
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
        :return: deleted item dict or None
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
        calculate total weight of all cargo items
        :return: float
        """
        return sum(ci.get("cargo_weight", 0) for ci in self.get_all_items())

    def get_all_items(self) -> list:
        """
        get all cargo items from DB
        :return: list
        """
        return self._db.get_all_items()

    def count_dangerous_cargo(self) -> int | None:
        """
        count items with danger_level > 0
        :return: int
        """
        dangerous_cargo = 0
        for itm in self.get_all_items():
            if itm["danger_level"] and itm["danger_level"] > 0:
                dangerous_cargo += 1
        return dangerous_cargo

    def _print_all_items(self):
        """
        prints all items
        :return:
        """
        for item in self.get_all_items():
            print(item)

    def _cut_the_process(self, value) -> bool | None:
        """
        check if value is ** (exit command)
        :param value:
        :return: bool | None
        """
        if value == "**":
            ErrorLogger.write_log("info", "Process stopped by user ", __name__)
            return True
        return None

    def get_cargo_planet_input(self) -> str | None:
        """
        process input
        trigger get_cargo_planet
        :return: string or None
        """
        planet = ""
        while True:
            inp = input("Enter Cargo planet: (Enter ** to exit)")
            planet = self.get_cargo_planet(inp)
            if self._cut_the_process(inp):
                return None
            if not planet:
                print("Please enter correct planet")
                continue
            else:
                planet = inp
                break
        return planet

    def get_cargo_name_input(self) -> None | str:
        """
        process input
        trigger get_cargo_name
        :return: string or None
        """
        cname = ""
        while True:
            inp = input("Enter Cargo Name: (Enter ** to exit)")
            if self._cut_the_process(inp):
                return None
            if not self.get_cargo_name(inp):
                print("Please enter correct name (longer than 2 characters)")
                continue
            else:
                cname = inp
                break
        return cname

    def get_cargo_weight_input(self) -> float | None:
        """
        process input
        trigger get_cargo_weight
        :return: float or None
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
        """
        process input
        trigger get_danger_level
        :return: int or None
        """
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
        """
        process input
        trigger get_requires_cooling
        :return: int or None
        """
        while True:
            try:
                requires_cooling = input(
                    "Is cargo requires cooling: (Enter ** to exit) \n possible values 1 | 0 \n"
                )

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
        """
        validate cargo name
        :param cname:
        :return: string or None
        """
        return validator.validate_name(cname)

    def get_cargo_weight(self, weight) -> float | None:
        """
        validate cargo weight
        :param weight:
        :return: float or None
        """
        return validator.validate_positive_numbers(weight)

    def get_cargo_planet(self, planet) -> str | None:
        """
        validate planet
        :param planet:
        :return: string or None
        """
        return validator.validate_planet(planet)

    def get_danger_level(self, danger_level) -> int | None:
        """
        validate danger level
        :param danger_level:
        :return: int or None
        """
        return validator.validate_danger_level(danger_level)

    def get_requires_cooling(self, cooling) -> int | None:
        """
        validate cooling level
        :param cooling:
        :return: int or None
        """
        return validator.validate_cooling_level(cooling)

    def get_cargo_by_planet(self, planet) -> list:
        """
        filter cargo by planet
        :param planet:
        :return: list
        """
        plt = validator.validate_planet(planet)
        cargo_by_planet = []
        if plt:
            for item in self.__cargo_items:
                if plt == item["cargo_origin_planet"]:
                    cargo_by_planet.append(item)

        return cargo_by_planet
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


        item_data = {
            "itemid": int(item.item_id),
            "cargo_weight": weight,
            "cargo_name": cargo_name,
            "requires_cooling" : requires_cooling,
            "danger_level" : danger_level
        }


        if db.insert_item(item_data):
            print("****Item Added****")
            ErrorLogger.write_log( f"Cargo Station: Item {int(item.item_id)} was added")

            self._print_all_items()
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
            return True
        return None


    def get_cargo_weight(self) -> float:
        cargo_weight = 0
        while True:
            try:
                cweight = input("Enter Cargo Weight: (Enter ** to exit) ").strip()

                if self._cut_the_process(cweight):
                    return False

                if not Validator.minimum_length(cweight, 2):
                    print("Cargo weight must be at least 2 characters")
                    continue

                cargo_weight = float(cweight)
                break

            except ValueError:
                print("Please enter numbers only")
        return cargo_weight

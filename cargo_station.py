import random

from cargo_item import CargoItem
from db import Db


class CargoStation:

    def __init__(self):
        self._db = Db()
        self._cargo_items = self._db.get_all_items()

    @property
    def cargo_items(self):
        return self._cargo_items

    @cargo_items.setter
    def cargo_items(self, cargo_items):
        self._cargo_items = cargo_items

    # def _get_all_ids(self):
    #     existins_ids = []
    #     for ci in self._cargo_items:
    #         existins_ids.append(ci.item_id)
    #     return existins_ids
    #
    # def _generate_id(self):
    #     return random.randint(1, 10)
    #
    # def _validate_id(self, item_id: int):
    #     if item_id in self._get_all_ids():
    #         return True
    #     return False




    def add_item(self, item: CargoItem):
        db = Db()



        if db.insert_item({"itemid": int(item.item_id), "name": item.cargo_name, "weight": item.cargo_weight,
                           "planet": item.cargo_origin_planet}):
            print("****Item Added****")
            self._print_all_items()
        else:
            print("Something went wrong")

    def remove_item(self, itemid):


        if self.find_item_by_id(itemid):
            self._db.delete_item(itemid)
            print("****Item Removed****")

            self._print_all_items()

        else:
            print("Item not found")


    def find_item_by_id(self, itemid):
        for ci in self.get_all_items():
            if ci["itemid"] == itemid:
                return ci
        return None


    def get_total_weight(self):
        total_weight = 0
        for ci in self._cargo_items:
            total_weight += ci.cargo_weight()
        return total_weight

    def get_all_items(self):
        return self._db.get_all_items()

    def _print_all_items(self):
        for item in self.get_all_items():
            print(item)

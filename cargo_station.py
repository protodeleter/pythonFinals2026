from db import Db


class CargoStation:

    def __init__(self):
        self._db = Db()
        self._cargo_items = self._db.get_all_items()

    @property
    def cargo_items(self):
        return self._cargo_items

    def add_item(self, item):
        db = Db()
        if db.insert_item({"itemid": str(item.item_id), "name": item.cargo_name, "weight": item.cargo_weight,
                           "planet": item.cargo_origin_planet}):
            print("****Item Added****")
            self._print_all_items()
        else:
            print("Something went wrong")

    def remove_item(self, itemid):
        self._db.delete_item(itemid)
        # self.cargo_items.remove(item)

    def find_item(self, item):
        for ci in self._cargo_items:
            if ci.cargo_name() == item.cargo_name() and ci.item_id() == item.item_id():
                return ci
        return None

    def get_total_weight(self):
        total_weight = 0
        for ci in self._cargo_items:
            total_weight += ci.cargo_weight()
        return total_weight

    def _print_all_items(self):
        for item in self._db.get_all_items():
            print(item)

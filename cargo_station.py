

class CargoStation:

    def __init__(self):
        self.cargo_items = []

    def add_item(self, item):
        self.cargo_items.append(item)

    def remove_item(self, item):
        self.cargo_items.remove(item)

    def find_item(self, item):
        for ci in self.cargo_items:
            if ci.cargo_name() == item.cargo_name() and ci.item_id() == item.item_id():
                return ci
        return None

    def get_total_weight(self):
        total_weight = 0
        for ci in self.cargo_items:
            total_weight += ci.cargo_weight()
        return total_weight
from validator import Validator

class CargoItem:



    def __init__(self, itemid, name, weight, origin_planet):
        self._itemid = itemid

        if Validator.minimum_length(name, 2):
            self._name = name

        self._weight = weight
        self.origin_planet = origin_planet

    @property
    def item_id(self):
        return self._itemid

    @property
    def cargo_name(self):
        return self._name

    @property
    def cargo_weight(self):
        return self._weight
    @property
    def cargo_origin_planet(self):
        return self.origin_planet

    def __str__(self):
        return "Cargo Item {} with weight {} and origin planet {}".format(self.item_id, self.cargo_weight, self.cargo_origin_planet)
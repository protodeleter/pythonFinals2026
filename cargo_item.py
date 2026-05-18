from generateid import GenerateID


class CargoItem:



    def __init__(self, name, weight, origin_planet):
        self._itemid = GenerateID.generate_id()

        self._name = name
        self._weight = weight
        self._origin_planet = origin_planet

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
        return self._origin_planet

    def __str__(self):
        return "Cargo Item with id {} named \"{}\" with weight {} and origin planet {}".format(self._itemid, self._name, self.cargo_weight, self.cargo_origin_planet)
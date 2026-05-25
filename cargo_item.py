import random

from db import Db


class CargoItem:



    def __init__(self, name, weight, origin_planet):

        self._itemid = self._assign_id()
        self._name = name
        self._weight = weight
        self._origin_planet = origin_planet


    @property
    def item_id(self) -> int:
        return self._itemid

    @property
    def cargo_name(self) -> str:
        return self._name

    @property
    def cargo_weight(self) -> float:
        return self._weight

    @property
    def cargo_origin_planet(self) -> str:
        return self._origin_planet

    def set_cargo_weight(self, weight: float) -> None:
        self._weight = weight

    def set_cargo_name(self, name: str) -> None:
        self._name = name

    def set_cargo_origin_planet(self, planet_name: str) -> None:
        self._origin_planet = planet_name

    def set_cargo_item_id(self) -> None:
        self._itemid = self._assign_id()


    def _assign_id(self) -> int:
        db = Db()
        return db.assign_id()


    def __str__(self) -> str:
        return "Cargo Item with id {} named \"{}\" with weight {} and origin planet {}".format(self._itemid, self._name,
                                                                                               self.cargo_weight,
                                                                                               self.cargo_origin_planet)


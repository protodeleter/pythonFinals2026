import random

from db import Db


class CargoItem:

    def __init__(self, name, weight, origin_planet):
        self.__itemid = self._assign_id()
        self.__name = name
        self.__weight = weight
        self.__origin_planet = origin_planet

    @property
    def item_id(self) -> int:
        """
        :return: _itemid
        """
        return self.__itemid

    @property
    def cargo_name(self) -> str:
        return self.__name

    @property
    def cargo_weight(self) -> float:
        return self.__weight

    @property
    def cargo_origin_planet(self) -> str:
        return self.__origin_planet

    def set_cargo_weight(self, weight: float) -> None:
        self.__weight = weight

    def set_cargo_name(self, name: str) -> None:
        self.__name = name

    def set_cargo_origin_planet(self, planet_name: str) -> None:
        self.__origin_planet = planet_name

    def set_cargo_item_id(self) -> None:
        self.__itemid = self._assign_id()

    def _assign_id(self) -> int:
        db = Db()
        return db.assign_id()

    def __str__(self) -> str:
        return "Cargo Item with id {} named \"{}\" with weight {} and origin planet {}".format(self._itemid, self._name,
                                                                                               self.cargo_weight,
                                                                                               self.cargo_origin_planet)

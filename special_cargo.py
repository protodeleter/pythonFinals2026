from typing import override

from cargo_item import CargoItem


class SpecialCargo(CargoItem):


    def __init__(self, name, weight, origin_planet, danger_level, requires_cooling):
        super().__init__(name, weight, origin_planet)
        self.name:str = name
        self.weight:float = weight
        self.origin_planet:str = origin_planet
        self._danger_level:int = danger_level
        self._requires_cooling:bool = requires_cooling

    @property
    def danger_level(self) -> int:
        return self._danger_level

    @danger_level.setter
    def danger_level(self, value) -> None:
        self._danger_level = value

    @property
    def requires_cooling(self) -> bool:
        return self._requires_cooling

    @requires_cooling.setter
    def requires_cooling(self, value) -> None:
        self._requires_cooling = value

    @property
    def weight(self) -> float:
        return self._weight
    @weight.setter
    def weight(self, value) -> None:
        self._weight = value
    @property
    def name(self) -> str:
        return self._name
    @name.setter
    def name(self, value) -> None:
        self._name = value

    def get_weight(self):
        return self.weight
    def get_name(self):
        return self.name

    def _validate_danger_level(self):
        if self.danger_level <= 0 or self.danger_level > 5:
            print("Please enter a valid danger level")
            return False
        return True

    @override
    def __str__(self):
        return super().__str__() + f" denger {self.danger_level} requires cooling {self.requires_cooling}"
from cargo_item import CargoItem


class SpecialCargo(CargoItem):
    """
    extended cargo type with danger level and cooling requirements
    """

    def __init__(self, name, weight, origin_planet, danger_level, requires_cooling):
        """
        initialize SpecialCargo
        extends CargoItem with danger_level and requires_cooling
        :param name:
        :param weight:
        :param origin_planet:
        :param danger_level:
        :param requires_cooling:
        """
        super().__init__(name, weight, origin_planet)
        self.name: str = name
        self.weight: float = weight
        self.origin_planet: str = origin_planet
        self._danger_level: int = danger_level
        self._requires_cooling: bool = requires_cooling

    @property
    def danger_level(self) -> int:
        """
        get danger level
        :return: int
        """
        return self._danger_level

    @danger_level.setter
    def danger_level(self, value) -> None:
        """
        set danger level
        :param value:
        :return:
        """
        self._danger_level = value

    @property
    def requires_cooling(self) -> bool:
        """
        get cooling requirement
        :return: bool
        """
        return self._requires_cooling

    @requires_cooling.setter
    def requires_cooling(self, value) -> None:
        """
        set cooling requirement
        :param value:
        :return:
        """
        self._requires_cooling = value

    @property
    def weight(self) -> float:
        """
        get weight
        :return: float
        """
        return self._weight

    @weight.setter
    def weight(self, value) -> None:
        """
        set weight
        :param value:
        :return:
        """
        self._weight = value

    @property
    def name(self) -> str:
        """
        get name
        :return: string
        """
        return self._name

    @name.setter
    def name(self, value) -> None:
        """
        set name
        :param value:
        :return:
        """
        self._name = value

    def get_weight(self):
        """
        return weight
        :return: float
        """
        return self.weight

    def get_name(self):
        """
        return name
        :return: string
        """
        return self.name

    def _validate_danger_level(self):
        """
        validate danger level (1–5)
        :return: bool
        """
        if self.danger_level <= 0 or self.danger_level > 5:
            print("Please enter a valid danger level")
            return False
        return True

    def __str__(self):
        """
        string representation of SpecialCargo
        :return: string
        """
        return (
            super().__str__()
            + f" danger {self.danger_level} requires cooling {self.requires_cooling}"
        )
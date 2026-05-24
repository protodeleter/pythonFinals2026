import unittest

import cargo_station
from cargo_item import CargoItem


class CargoStationTests(unittest.TestCase):


    def test_get_cargo_name(self):
        self.cargo_station = cargo_station.CargoStation()

        self.assertEqual(self.cargo_station.get_cargo_name(), "Cargo")

    def test_add_item(self):
        self.cargo_station = cargo_station.CargoStation()

        self.cargo_item = CargoItem()

        self.cargo_station.add_item("Cargo")

if __name__ == "__main__":
    unittest.main()
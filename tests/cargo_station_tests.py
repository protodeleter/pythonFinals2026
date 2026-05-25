import unittest

import exceptions
from cargo_station import CargoStation
from cargo_item import CargoItem
from special_cargo import SpecialCargo


class CargoStationTests(unittest.TestCase):



    def test_cargo_item(self):
        name = "Cargo"
        weight = 10
        origin_planet = "some planet"
        cargo_item = CargoItem(name,weight,origin_planet)

        self.assertEqual("Cargo", cargo_item.cargo_name , "Cargo item name is wrong")
        self.assertEqual(10, cargo_item.cargo_weight , "Cargo item name is wrong")
        self.assertEqual("some planet", cargo_item.cargo_origin_planet , "Cargo item name is wrong")

    def test_add_item(self):
        name = "Cargo"
        weight = 10
        origin_planet = "some planet"
        cargo_item = CargoItem(name,weight,origin_planet)
        cs = CargoStation()
        res = cs.add_item(cargo_item)
        item = cs.find_item_by_id(res["itemid"])

        self.assertEqual(item["cargo_name"], cargo_item.cargo_name , "Cargo item name is wrong")
        self.assertEqual(item["cargo_weight"], cargo_item.cargo_weight , "Cargo item name is wrong")
        self.assertEqual(item["cargo_origin_planet"], cargo_item.cargo_origin_planet , "Cargo item name is wrong")
        self.assertIsNone(None, res["requires_cooling"])
        self.assertIsNone(None, res["danger_level"])



    def test_add_special_item(self):
        name = "Cargo"
        weight = 10
        origin_planet = "some planet"
        requires_cooling = 1
        danger_level = 1

        cargo_item = SpecialCargo(name,weight,origin_planet,requires_cooling,danger_level)
        cs = CargoStation()
        res = cs.add_item(cargo_item)
        item = cs.find_item_by_id(res["itemid"])
        self.assertEqual(item["cargo_name"], cargo_item.cargo_name , "Cargo item name is wrong")
        self.assertEqual(item["cargo_weight"], cargo_item.cargo_weight , "Cargo item name is wrong")
        self.assertEqual(item["cargo_origin_planet"], cargo_item.cargo_origin_planet , "Cargo item name is wrong")
        self.assertEqual(item["requires_cooling"], cargo_item.requires_cooling , "Cargo requires cooling is wrong")
        self.assertEqual(item["danger_level"], cargo_item.danger_level , "Cargo danger level is wrong")


    def test_cargo_name_wrong_name(self):
        cargo_station = CargoStation()
        self.assertRaises( exceptions.CargoNameError, lambda: cargo_station.get_cargo_name("c") )

    def test_cargo_name_returns_string(self):
        cargo_station = CargoStation()
        res = cargo_station.get_cargo_name("cargo")
        self.assertIsInstance(res, str , "should return a string")

    def test_cargo_name_correct_name(self):
        cargo_station = CargoStation()
        name = "Cargo"
        self.assertEqual( cargo_station.get_cargo_name(name), name, "Cargo name is wrong")
        self.assertIsInstance(name, str, "Should be a string")


if __name__ == "__main__":
    unittest.main()
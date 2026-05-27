import unittest

import exceptions
from cargo_station import CargoStation
from cargo_item import CargoItem
from special_cargo import SpecialCargo


class CargoStationTests(unittest.TestCase):

    def test_cargo_item(self):
        cargo_item = CargoItem("Cargo", 10, "some planet")

        self.assertEqual("Cargo", cargo_item.cargo_name)
        self.assertEqual(10, cargo_item.cargo_weight)
        self.assertEqual("some planet", cargo_item.cargo_origin_planet)

    def test_add_item(self):
        cargo_item = CargoItem("Cargo", 10, "some planet")

        cs = CargoStation()
        res = cs.add_item(cargo_item)

        item = cs.find_item_by_id(res["itemid"])

        self.assertEqual(cargo_item.cargo_name, item["cargo_name"])
        self.assertEqual(cargo_item.cargo_weight, item["cargo_weight"])
        self.assertEqual(cargo_item.cargo_origin_planet, item["cargo_origin_planet"])

        self.assertIsNone(item["requires_cooling"])
        self.assertIsNone(item["danger_level"])



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
        name = "c"
        result = cargo_station.get_cargo_name(name)
        self.assertIsNone(result, "Cargo name is wrong")

    def test_cargo_name_correct_name(self):
        cargo_station = CargoStation()
        name = "Cargo"
        result = cargo_station.get_cargo_name(name)

        self.assertEqual( cargo_station.get_cargo_name(name), name, "Cargo name is wrong")
        self.assertIsInstance(result, str)


    def test_cargo_weight_not_float(self):
        cargo_station = CargoStation()
        weight = "error"
        self.assertIsNone(cargo_station.get_cargo_weight(weight), "Cargo weight is not correct")

    def test_cargo_weight_float(self):
        cargo_station = CargoStation()
        result = cargo_station.get_cargo_weight("10.5")
        self.assertEqual(10.5, result)

    def test_cargo_weight_zero(self):
        cargo_station = CargoStation()
        result = cargo_station.get_cargo_weight(0)
        self.assertIsNone(result)


    def test_cargo_planet_correct(self):
        cargo_station = CargoStation()
        planet = "some planet"
        self.assertEqual(cargo_station.get_cargo_planet(planet), planet, "Should be correct")

    def test_cargo_planet_wrong(self):
        cargo_station = CargoStation()
        planet = ""
        self.assertIsNone(cargo_station.get_cargo_planet(planet), "Should be None")

    def test_cargo_cooling_correct(self):
        cargo_station = CargoStation()
        cooling = 1
        self.assertEqual( cargo_station.get_requires_cooling(cooling), cooling, "Should be correct" )

    def test_cargo_cooling_wrong(self):
        cargo_station = CargoStation()
        cooling = 5
        self.assertIsNone(cargo_station.get_requires_cooling(cooling), "Should be None")

    def test_remove_cargo_item_(self):
        cargo_station = CargoStation()
        with self.assertRaises(exceptions.CargoNotFoundError) as cm:
            cargo_station.remove_item(9999)
        the_exception = cm.exception
        self.assertEqual(the_exception, 3)
        self.assertRaises(exceptions.CargoNotFoundError)

if __name__ == "__main__":
    unittest.main()
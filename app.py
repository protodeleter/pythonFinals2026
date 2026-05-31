class App:
    def __init__(self, cargo_station):
        """
        initialize App
        :param cargo_station: CargoStation instance
        :return:
        """
        self._cs = cargo_station

    def _cut_the_process(self, value):
        """
        check if user typed exit command (**)
        :param value:
        :return: False or None
        """
        if value == "**":
            return False
        return None

    def _add_cargo(self) -> dict | bool:
        """
        add cargo workflow
        triggers CargoStation input methods
        creates CargoItem or SpecialCargo
        :return: dict (added item) or False
        """
        ErrorLogger.write_log("info", "Add cargo started", __name__)

        speacial_cargo_flag = False
        is_special_cargo = input("Is it special cargo? (Y) ")
        if is_special_cargo in ("Y", "y"):
            speacial_cargo_flag = True
            ErrorLogger.write_log("info", "Special cargo", __name__)

        cname = self._cs.get_cargo_name_input()
        if cname is None:
            return False
        ErrorLogger.write_log("info", "Cargo name " + cname, __name__)

        cweight = self._cs.get_cargo_weight_input()
        if cweight is None:
            return False
        ErrorLogger.write_log("info", "Cargo weight " + str(cweight), __name__)

        cplanet = self._cs.get_cargo_planet_input()
        if not cplanet:
            return False
        ErrorLogger.write_log("info", "Cargo planet " + cplanet, __name__)

        if speacial_cargo_flag:
            danger_level = self._cs.get_danger_level_inp()
            if danger_level is None:
                return False
            ErrorLogger.write_log("info", "Cargo danger level " + str(danger_level), __name__)

            requires_cooling = self._cs.get_requires_cooling_inp()
            if requires_cooling is None:
                return False
            ErrorLogger.write_log("info", "Cargo requires_cooling " + str(requires_cooling), __name__)

            ci = SpecialCargo(cname, cweight, cplanet, danger_level, requires_cooling)
        else:
            ci = CargoItem(cname, cweight, cplanet)

        res = self._cs.add_item(ci)
        if res:
            print("****Item Added****")

        self._show_all_items()
        return res

    def _remove_cargo(self) -> bool:
        """
        remove cargo workflow
        triggers CargoStation.remove_item
        :return: bool
        """
        ErrorLogger.write_log("info", "Remove cargo started", __name__)
        print("*** Remove Cargo Item ***")
        items = self._cs.get_all_items()
        print(items)

        while True:
            itm = input("Enter item id: (type ** to main menu) ")
            if itm == "**":
                self._main_menu()
                return False

            if self._cs.remove_item(itm):
                print(f"****Item {itm} Removed****")
            else:
                print("****Item not found****")
            return True

    def _find_cargo(self):
        """
        find cargo workflow
        triggers CargoStation.find_item_by_id
        :return: bool or None
        """
        print("*** Find Cargo Item ***")
        while True:
            try:
                itm = input("Enter item id: (type ** to main menu) ")
                if itm == "**":
                    self._main_menu()
                    return None

                itm = int(itm)
                item = self._cs.find_item_by_id(itm)
                print(item)
                return True

            except ValueError:
                print("Please enter numbers only")

            except CargoNotFoundError as e:
                print("****")
                print(e)
                print("****")
                return False

    def _show_total_weight(self) -> None:
        """
        show total weight of all cargo
        :return: None
        """
        print("*** Show Total Weight ***")
        print(f"Total weight is {self._cs.get_total_weight()} ")

    def _show_all_items(self) -> None:
        """
        print all cargo items
        :return: None
        """
        print("**** All Items ***")
        for item in self._cs.get_all_items():
            print(
                f'Item id: {item["itemid"]} | name: {item["cargo_name"]} | weight: {item["cargo_weight"]} | '
                f'planet: {item["cargo_origin_planet"]} | danger_level: {item["danger_level"]} | '
                f'requires_cooling: {item["requires_cooling"]}'
            )

    def _filter_by_planet(self) -> None:
        """
        filter cargo by planet
        :return: None
        """
        planet = ""
        while True:
            itm = input("Enter Cargo planet: (type ** to main menu) ")
            if itm == "**":
                self._main_menu()
                return None

            if not validator.minimum_length(itm, 1):
                print("Planet must be at least 1 character")
                continue

            planet = itm
            break

        for item in self._cs.get_cargo_by_planet(planet):
            print(
                f'Item id: {item["itemid"]} | name: {item["cargo_name"]} | weight: {item["cargo_weight"]} | '
                f'planet: {item["cargo_origin_planet"]} | danger_level: {item["danger_level"]} | '
                f'requires_cooling: {item["requires_cooling"]}'
            )

        return None

    def _count_dangerous_cargo(self) -> None:
        """
        count items with danger_level > 0
        :return: None
        """
        print("*** Count Dangerous Cargo ***")
        print(self._cs.count_dangerous_cargo())
        return None

    def _main_menu(self) -> None:
        """
        main menu loop
        handles user navigation
        :return: None
        """
        while True:
            cs = CargoStation()
            items = cs.get_all_items()

            main_menu = "1: Add cargo item \n"
            if items:
                main_menu += "2: Remove cargo item\n"
                main_menu += "3: Find cargo item\n"
                main_menu += "4: Show total weight\n"
                main_menu += "5: Show all items \n"
                main_menu += "6: Filter by planet \n"
                main_menu += "7: Count dangerous cargo \n"

            main_menu += "8: Exit"

            try:
                option = input('Choose an option: \n' + main_menu)
                op = int(option)

                if op == 1:
                    self._add_cargo()
                if op == 2 and items:
                    self._remove_cargo()
                if op == 3 and items:
                    self._find_cargo()
                if op == 4 and items:
                    self._show_total_weight()
                if op == 5 and items:
                    self._show_all_items()
                if op == 6 and items:
                    self._filter_by_planet()
                if op == 7 and items:
                    self._count_dangerous_cargo()
                if op == 8:
                    exit(0)

            except ValueError:
                print("Please enter numbers only")

    def run(self):
        """
        start application
        :return: None
        """
        self._main_menu()
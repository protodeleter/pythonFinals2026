# This is a sample Python script.
from app import App
from cargo_item import CargoItem
from cargo_station import CargoStation
from db import Db
from error_logger import ErrorLogger
from validator import Validator
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.




import json
#


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    obj = App(CargoStation())
    App.run(obj)

    # db = Db()
    # print(not db.get_all_items())


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

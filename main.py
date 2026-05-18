# This is a sample Python script.
from app import App
from cargo_item import CargoItem
from db import Db
from validator import Validator
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.




import json
#


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # obj = App()
    # App.run(obj)

    ci = CargoItem(12, "test", "12" ,"mars")

    db = Db()
    db.insert_item(ci)
    print(ci)
    # print(Validator.minimum_length("f", 2))
    # Open and load the file
    with open('db.json', 'r') as file:
        data = json.load(file)
        print(data[0]["itemid"])


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

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
    obj = App()
    App.run(obj)

    # ci = CargoItem("test", "12" ,"mars")

    # print(ci)
    # print(Validator.minimum_length("f", 2))
    # Open and load the file

    # with open('db.json', 'r') as file:
    #     data = json.load(file)
    #     nnn = data
    #     # print(data)
    #     #  data.append({ "itemid" : str(ci.item_id), "name" : ci.cargo_name, "weight" : ci.cargo_weight, "planet" : ci.cargo_origin_planet})
    #     # print(data)
    # print(data)
    # data.append({ "itemid" : str(ci.item_id), "name" : ci.cargo_name, "weight" : ci.cargo_weight, "planet" : ci.cargo_origin_planet})
    # print(data)

    # with open("db.json", "w", encoding="utf-8") as file:
    #     json.dump(data, file, indent=4)


    # sss = { "itemid" : str(ci.item_id), "name" : ci.cargo_name, "weight" : ci.cargo_weight, "planet" : ci.cargo_origin_planet}
    #
    # db = Db()
    # # db.insert_item( sss )
    #
    # print(db.get_item_by_id("23289788-6ab1-42b5-9728-6f5c25fe05a9"))

    # db.delete_item("86be06de-e5a2-4a42-8a82-ad53c5ee4fe3")
    # print(ci.item_id)
    #
    # print(json.dumps([ ]))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

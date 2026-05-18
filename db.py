import json
import os


class Db:
    def __init__(self):

        if os.path.exists("db.json") and os.path.getsize("db.json") == 0:
            self._fix_empty_db()
        with open('db.json', 'r') as file:
            self._dbfile = json.load(file)

    def _fix_empty_db(self):
        with open("db.json", "w", encoding="utf-8") as file:
            file.write("[]")

    def insert_item(self, item: dict) -> None:
        self._dbfile.append(item)
        self._update_db()


    def delete_item(self, itemid:int) -> None:
        for item in self._dbfile:
            if item["itemid"] == itemid:
                self._dbfile.remove(item)
        self._update_db()


    def _update_db(self) -> None:
        with open("db.json", "w", encoding="utf-8") as file:
            json.dump(self._dbfile, file, indent=4)

    def get_item_by_id(self, itemid:str) -> dict:
        for item in self._dbfile:
            if item["itemid"] == itemid:
                return item
        return {}



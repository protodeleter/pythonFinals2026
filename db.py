import json
import os


class Db:
    _file = "db.json"

    def __init__(self):
        self._dbfile = self._load_db()

    def _load_db(self):
        if not os.path.exists(self._file):
            self._fix_empty_db()
        if os.path.getsize(self._file) == 0:
            self._fix_empty_db()
        try:
            with open(self._file, "r", encoding="utf-8") as file:
                data = json.load(file)

            if not isinstance(data, list):
                print("DB file must contain a JSON array")
                self._fix_empty_db()
                return []

            return data

        except json.JSONDecodeError:
            print("DB file has wrong JSON format")
            self._fix_empty_db()
            return []

    def _fix_empty_db(self):
        with open(self._file, "w", encoding="utf-8") as file:
            json.dump([], file, indent=4)

    def insert_item(self, item: dict) -> bool:
        self._dbfile.append(item)
        if self._update_db():
            return True
        return False

    def delete_item(self, itemid: str) -> None:
        for item in self._dbfile:
            if item["itemid"] == itemid:
                self._dbfile.remove(item)
        self._update_db()

    def _update_db(self) -> bool:
        with open(self._file, "w", encoding="utf-8") as file:
            try:
                json.dump(self._dbfile, file, indent=4)
                return True
            except json.JSONDecodeError:
                return False

    def get_item_by_id(self, itemid: str) -> dict:
        for item in self._dbfile:
            if item["itemid"] == itemid:
                return item
        return {}

    def get_all_items(self):
        items = []
        for item in self._dbfile:
            items.append(item)
        return items

import json
import os

from error_logger import ErrorLogger


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

    def _fix_empty_db(self) -> None:
        with open(self._file, "w", encoding="utf-8") as file:
            json.dump([], file, indent=4)
        ErrorLogger.write_log( "Info" , f"DB : {self._file} was found broken and has been fixed." , __name__ )

    def insert_item(self, item: dict) -> dict:
        self._dbfile.append(item)
        if self._update_db():
            return item
        return {}

    def delete_item(self, item) -> dict:
        for itm in self._dbfile:
            if itm.get("itemid") == item["itemid"]:
                self._dbfile.remove(item)
                return item
        self._update_db()
        return {}

    def _update_db(self) -> bool:
        try:
            with open(self._file, "w", encoding="utf-8") as file:
                json.dump(self._dbfile, file, indent=4)
                ErrorLogger.write_log( "info" ,"DB updated" , __name__ )

            return True

        except TypeError as e:
            print("Data cannot be converted to JSON:", e)

            return False

        except OSError as e:
            print("File write error:", e)
            return False

    def get_item_by_id(self, itemid: str) -> dict:
        for item in self._dbfile:
            if item.get("itemid") == itemid:
                return item
        return {}

    def get_all_items(self) -> list:
        with open( self._file, 'r') as file:
            data = json.load(file)
        return data


    def _get_max_id(self) -> int:
        max_id = 0
        with open(self._file, 'r') as file:
            data = json.load(file)
            for item in data:
                max_id = max(max_id, int(item["itemid"]))

        return max_id

    def _increment_max_id(self) -> int:
        self._max_id = self._get_max_id() + 1
        return self._max_id

    def assign_id(self):
        return self._increment_max_id()




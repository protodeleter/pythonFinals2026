import json


class Db:
    def __init__(self):
        self._dbfile = open('db.json', 'r')

    def insert_item(self, item):
        self._dbfile.seek(0)
        self._dbfile.truncate()
        self._dbfile.write(json.dumps(item))

    def delete_item(self, item):
        self._dbfile.seek(0)
        self._dbfile.truncate()
        self._dbfile.write(json.dumps(item))

    def get_item(self, item):
        self._dbfile.seek(0)
        self._dbfile.truncate()
        self._dbfile.write(json.dumps(item))

    def update_item(self, item):
        self._dbfile.seek(0)
        self._dbfile.truncate()
        self._dbfile.write(json.dumps(item))

import json
import os
import time


class ErrorLogger:

    _file = "log.txt"

    def __init__(self):
        self._logfile = self._load_log()

    def _load_log(self):
        if not os.path.exists(self._file):
            with open(self._file, "a") as f:
                pass  # File is created and immediately closed

    def write_log(self, message):
        with open(self._file, "a") as f:
            f.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ": " + message + "\n")
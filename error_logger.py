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

    def get_file(self):
        return self._file

    @staticmethod
    def write_log( error ,message , method):
        with open(ErrorLogger._file, "a") as f:
            f.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ": " +  error + " | "  + message +" | "+ method + "\n")
import os
import time

import os
import time


class ErrorLogger:

    _file = "log.txt"

    def __init__(self):
        """
        initialize logger
        ensure log file exists
        :return:
        """
        self._logfile = self._load_log()

    def _load_log(self):
        """
        create log file if missing
        :return: None
        """
        if not os.path.exists(self._file):
            with open(self._file, "a") as f:
                pass  # create empty file

    def get_file(self):
        """
        return log file name
        :return: string
        """
        return self._file

    @staticmethod
    def write_log(error, message, method):
        """
        write log entry to log.txt
        :param error: error level (info, warning, error)
        :param message: log message
        :param method: method name
        :return: None
        """
        with open(ErrorLogger._file, "a") as f:
            f.write(
                time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                + ": "
                + error
                + " | "
                + message
                + " | "
                + method
                + "\n"
            )
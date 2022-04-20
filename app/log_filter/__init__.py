import logging


class FilterDebug(logging.Filter):
    def filter(self, record):
        if record.levelno == 10:
            return True
        else:
            return False
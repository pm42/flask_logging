import logging
from flask import has_request_context

class FilterDebug(logging.Filter):
    def filter(self, record):
        if record.levelno == 10:
            return True
        else:
            return False


class FilterInfo(logging.Filter):
    def filter(self, record):
        if record.levelno == 20 and has_request_context():
            return True
        else:
            return False
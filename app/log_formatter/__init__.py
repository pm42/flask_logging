import logging
from flask import has_request_context, request
from rfc3339 import rfc3339
import datetime
import time
from flask import g


class RequestFormatter(logging.Formatter):
    def format(self, record):
        if has_request_context():

            now = time.time()
            duration = round(now - g.start, 2)
            dt = datetime.datetime.fromtimestamp(now)
            timestamp = rfc3339(dt, utc=True)

            record.url = request.url
            record.time = timestamp
            record.remote_addr = request.remote_addr
            record.request_method = request.method
            record.request_path = request.path
            record.ip = request.headers.get('X-Forwarded-For', request.remote_addr)
            record.host = request.host.split(':', 1)[0]
            record.args = dict(request.args)
            record.duration = duration

            request_id = request.headers.get('X-Request-ID')
            if request_id:
                record.id = request_id
            else:
                record.id = None

        else:
            record.url = None
            record.remote_addr = None
            record.request_method = None
            record.duration = None
            record.time = None

        return super().format(record)
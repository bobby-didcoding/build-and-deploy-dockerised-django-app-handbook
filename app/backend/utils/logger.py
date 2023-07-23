# --------------------------------------------------------------
# Python imports
# --------------------------------------------------------------
import copy
import errno
import logging
import os
import threading
from datetime import datetime
from logging.handlers import RotatingFileHandler
from uuid import uuid4

# --------------------------------------------------------------
# 3rd party imports
# --------------------------------------------------------------
import arrow
from pythonjsonlogger import jsonlogger

logging._shared_extra = threading.local()


class courseLogger(logging.Logger):
    def __init__(self, *args, **kwargs):
        super(courseLogger, self).__init__(*args, **kwargs)

    def makeRecord(
        self,
        name,
        level,
        fn,
        lno,
        msg,
        args,
        exc_info,
        func=None,
        extra=None,
        sinfo=None,
    ):
        if extra is not None:
            # Based on required format we need to make sure that any extra information is placed in "data" section.
            extra = {"data": extra}

        return super(courseLogger, self).makeRecord(
            name, level, fn, lno, msg, args, exc_info, func, extra, sinfo
        )


class BetterRotatingFileHandler(RotatingFileHandler):
    def _open(self):
        self._ensure_dir(os.path.dirname(self.baseFilename))
        return logging.handlers.RotatingFileHandler._open(self)

    def _ensure_dir(self, path):
        # type: (AnyStr) -> None
        """os.path.makedirs without EEXIST."""
        try:
            os.makedirs(path)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise


class courseJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(courseJsonFormatter, self).add_fields(log_record, record, message_dict)

        shared_extra = logging.get_shared_extra()
        if len(shared_extra) > 0:
            current_data = {"data": copy.deepcopy(log_record.get("data", {}))}
            shared_extra = copy.deepcopy(shared_extra)
            shared_extra = {**shared_extra, **current_data}
            log_record.update(shared_extra)

        if not log_record.get("dateCreated"):
            now = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f")
            log_record["dateCreated"] = now

        if log_record.get("level"):
            log_record["level"] = log_record["level"].upper()
        else:
            log_record["level"] = record.levelname

        if log_record.get("startProcessingTimer"):
            if not log_record.get("duration") and log_record.get("data", {}).get(
                "logGlobalDuration"
            ):
                log_record["duration"] = log_record["startProcessingTimer"].duration()
                del log_record["data"]["logGlobalDuration"]

            del log_record["startProcessingTimer"]

        log_record["app"] = {"name": "course", "threadName": record.threadName}

        self._move_unexpected_params_to_data(log_record)

    def _move_unexpected_params_to_data(self, log_record):
        top_level_attributes = [
            "dateCreated",
            "level",
            "duration",
            "message",
            "requestId",
            "customer",
            "app",
            "data",
        ]
        for key, _ in log_record.copy().items():
            if key not in top_level_attributes:
                if not log_record.get("data"):
                    log_record["data"] = {}

                log_record["data"][key] = log_record.get(key)
                del log_record[key]


class RequestIdGenerator:
    @staticmethod
    def get() -> str:
        return str(uuid4())


class Timer:
    def __init__(self):
        self._start = arrow.utcnow()

    def __str__(self):
        return self._start

    def duration(self):
        return int((arrow.utcnow() - self._start).microseconds / 1000)


def set_shared_extra(attributes: dict):
    for key, value in attributes.items():
        setattr(logging._shared_extra, key, value)


logging.set_shared_extra = set_shared_extra
del set_shared_extra


def init_shared_extra(request_id=None):
    logging.set_shared_extra(
        {
            "requestId": request_id if request_id else RequestIdGenerator.get(),
            "startProcessingTimer": Timer(),
        }
    )


logging.init_shared_extra = init_shared_extra
del init_shared_extra


def get_shared_extra() -> dict:
    results = {}
    for x in dir(logging._shared_extra):
        if x.startswith("__"):
            continue
        results[x] = getattr(logging._shared_extra, x)

    return results


logging.get_shared_extra = get_shared_extra
del get_shared_extra


def get_shared_extra_param(key: str):
    return logging.get_shared_extra().get(key, None)


logging.get_shared_extra_param = get_shared_extra_param
del get_shared_extra_param

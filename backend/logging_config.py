import logging
import logging.config
import sys

from backend.middleware.request_id import correlation_id_var, request_id_var


class RequestContextFilter(logging.Filter):
    """Injects request_id and correlation_id into every log record."""

    def filter(self, record: logging.LogRecord) -> bool:
        record.request_id = request_id_var.get()
        record.correlation_id = correlation_id_var.get()
        return True


def configure_logging(environment: str) -> None:
    is_dev = environment == "DEV"
    level = logging.DEBUG if is_dev else logging.INFO

    fmt = (
        "%(asctime)s | %(levelname)-8s | corr=%(correlation_id)s req=%(request_id)s | %(name)s | %(message)s"
        if is_dev
        else "%(asctime)s %(levelname)s corr=%(correlation_id)s req=%(request_id)s %(name)s %(message)s"
    )

    config = {
        "version": 1,
        "disable_existing_loggers": False,
        "filters": {
            "request_context": {"()": RequestContextFilter},
        },
        "formatters": {
            "default": {
                "format": fmt,
                "datefmt": "%Y-%m-%d %H:%M:%S",
            },
        },
        "handlers": {
            "default": {
                "class": "logging.StreamHandler",
                "stream": sys.stdout,
                "formatter": "default",
                "filters": ["request_context"],
            },
        },
        "loggers": {
            "backend": {
                "handlers": ["default"],
                "level": level,
                "propagate": False,
            },
            "uvicorn": {
                "handlers": ["default"],
                "level": level,
                "propagate": False,
            },
            "uvicorn.error": {
                "handlers": ["default"],
                "level": level,
                "propagate": False,
            },
            "uvicorn.access": {
                "handlers": ["default"],
                "level": "INFO",
                "propagate": False,
            },
            "tortoise": {
                "handlers": ["default"],
                "level": "INFO",
                "propagate": False,
            },
        },
        "root": {
            "handlers": ["default"],
            "level": "WARNING",
        },
    }

    logging.config.dictConfig(config)

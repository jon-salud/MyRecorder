import os
from pathlib import Path

# Base directories
BASE_DIR = Path(__file__).parent.parent.parent
RECORDINGS_DIR = os.path.join(BASE_DIR, "recordings")
LOGS_DIR = os.path.join(BASE_DIR, "logs")

# Logging configuration
LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
        },
    },
    "handlers": {
        "file": {
            "class": "logging.FileHandler",
            "filename": os.path.join(LOGS_DIR, "recorder.log"),
            "formatter": "standard"
        }
    },
    "root": {
        "handlers": ["file"],
        "level": "INFO",
    }
}

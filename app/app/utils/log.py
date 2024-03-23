import logging
import os
from pathlib import Path
from django.conf import settings


class Logger:
    logger: logging.Logger
    format = "%(asctime)s [%(levelname)8s] %(message)s"

    def __init__(
        self,
        file_path: str = settings.LOG_PATH,
        file_name: str = settings.LOG_FILE_NAME,
        level: int = logging.DEBUG,
        format: str = "",
    ):
        if not os.path.exists(file_path):
            os.mkdir(file_path)

        if not format:
            format = self.format

        formatter = logging.Formatter(format)

        streamingHandler = logging.StreamHandler()
        streamingHandler.setFormatter(formatter)
        file_handler = logging.FileHandler(file_path + file_name)
        file_handler.setFormatter(formatter)

        logging.basicConfig(handlers=[streamingHandler, file_handler], level=level)
        self.logger = logging.getLogger()


logger = Logger()
log = logger.logger

import logging
import os
from datetime import datetime


LOGGING_LOCATION = os.environ['HOME'] + '/logs/'
if not os.path.exists(LOGGING_LOCATION):
    try:
        os.makedirs(LOGGING_LOCATION)
    except Exception as e:
        print(e)

LOG_FILE_NAME = str(datetime.now()).replace('-', '').replace(':', '').replace(' ', '').split('.')[0] + '.log'


def create_logger(app_name="app_log"):
    logger = logging.getLogger(app_name)
    LOGGING_LEVEL=logging.INFO
    logger.setLevel(LOGGING_LEVEL)

    _logfile = LOGGING_LOCATION +  app_name + '_' + LOG_FILE_NAME

    fh = logging.FileHandler(_logfile)
    fh.setLevel(LOGGING_LEVEL)

    ch = logging.StreamHandler()
    ch.setLevel(LOGGING_LEVEL)

    ch = logging.StreamHandler()
    log_format_str = "%(asctime)s - [%(filename)s - %(funcName)10s():%(lineno)s ] - %(levelname)s - %(message)s"
    formatter = logging.Formatter(log_format_str, datefmt='%Y-%m-%d %H:%M:%S')

    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger


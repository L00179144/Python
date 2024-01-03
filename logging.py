"""
Author : Raghul Gopalakrishnan
Contact : raghulgk@gmail.com
Purpose : Tutorials and demonstration for time and logging in python programming
Pre-requisites : Python3 installation.
"""

import sys
import logging
#pip install colorlog
import colorlog
#pip install python-json-logger
from pythonjsonlogger import jsonlogger


#logging

logging.debug("A debug message")
logging.info("An info message")
logging.warning("A warning message")
logging.error("An error message")
logging.critical("A critical message")


logger = logging.getLogger("example")

stdout = colorlog.StreamHandler(stream=sys.stdout)

fmt = colorlog.ColoredFormatter(
    "%(name)s: %(white)s%(asctime)s%(reset)s | %(log_color)s%(levelname)s%(reset)s | %(blue)s%(filename)s:%(lineno)s%(reset)s | %(process)d >>> %(log_color)s%(message)s%(reset)s"
)

stdout.setFormatter(fmt)
logger.addHandler(stdout)

logger.setLevel(logging.DEBUG)

logger.debug("A debug message")
logger.info("An info message")
logger.warning("A warning message")
logger.error("An error message")
logger.critical("A critical message")

#logging to a file

logger = logging.getLogger(__name__)

stdoutHandler = logging.StreamHandler(stream=sys.stdout)
fileHandler = logging.FileHandler("logs.txt")

stdoutFmt = logging.Formatter(

    "%(name)s: %(asctime)s | %(levelname)s | %(filename)s:%(lineno)s | %(process)d >>> %(message)s"

)


jsonFmt = jsonlogger.JsonFormatter(
    "%(name)s %(asctime)s %(levelname)s %(filename)s %(lineno)s %(process)d %(message)s",
    rename_fields={"levelname": "severity", "asctime": "timestamp"},
    datefmt="%Y-%m-%dT%H:%M:%SZ",
)

stdoutHandler.setFormatter(stdoutFmt)

fileHandler.setFormatter(jsonFmt)

logger.addHandler(stdoutHandler)
logger.addHandler(fileHandler)

logger.setLevel(logging.DEBUG)

logger.debug("A debug message")
logger.error("An error message")
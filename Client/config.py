import logging
import os
from enum import Enum

# define the run mode of the server ------------------------------#
class RunMode(Enum):
    DEFAULT = 1
    DEBUG = 2
    LOCAL = 3
# ----------------------------------------------------------------#


# define the output of the logger --------------------------------#
class OUTPUT(Enum):
    FILE = 1
    CONSOLE = 2
    BOTH = 3
# ---------------------------------------------------------------#

# set the configurations ----------------------------------------#
# here are fixed configurations
NAME = "Client" # log name not necessary
LOG_DIR = "logs" # dir of logs
TRAIN_DATA_DIR = "../data/femnist/train"
TEST_DATA_DIR = "../data/femnist/test"

# here are changeable configurations
configurations = {
    RunMode.DEFAULT: {
        "LOGLEVEL": logging.INFO,
        "LOGOUTPUT": OUTPUT.BOTH,
        "LOGFILE_NAME": "client.log",
        "CLEAR_LOGFILE": True,
        "SERVER_HOST": "localhost",
        "SERVER_PORT": 6060
    },
    RunMode.DEBUG: {
        "LOGLEVEL": logging.DEBUG,
        "LOGOUTPUT": OUTPUT.BOTH,
        "LOGFILE_NAME": "client_debug.log",
        "CLEAR_LOGFILE": True,
        "SERVER_HOST": "localhost",
        "SERVER_PORT": 6060
    },
    RunMode.LOCAL: {
        "LOGLEVEL": logging.DEBUG,
        "LOGOUTPUT": OUTPUT.BOTH,
        "LOGFILE_NAME": "client_local.log",
        "CLEAR_LOGFILE": True,
        "SERVER_HOST": "localhost",
        "SERVER_PORT": 6060
    }
}
# ---------------------------------------------------------------#

# set the run mode ----------------------------------------------#
RUNMODE = RunMode.LOCAL
# ---------------------------------------------------------------#

# get the configurations ----------------------------------------#
try:
    config = configurations[RUNMODE]
    LOGLEVEL = config["LOGLEVEL"]
    LOGOUTPUT = config["LOGOUTPUT"]
    LOGFILE_NAME = config["LOGFILE_NAME"]
    CLEAR_LOGFILE = config["CLEAR_LOGFILE"]
    SERVER_HOST = config["SERVER_HOST"]
    SERVER_PORT = config["SERVER_PORT"]
    LOGFILE_ROUTES = LOG_DIR + "/" + LOGFILE_NAME

    if not os.path.exists(LOG_DIR):
        os.mkdir(LOG_DIR)

    if CLEAR_LOGFILE and os.path.exists(LOGFILE_ROUTES):
        with open(LOGFILE_ROUTES, "w") as f:
            f.write("")

except KeyError:
    raise Exception("Unknown run mode")
# ---------------------------------------------------------------#
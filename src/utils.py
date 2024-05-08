import os
import logging
from logging.config import fileConfig


fileConfig('logging_config.ini')
logger = logging.getLogger()

path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
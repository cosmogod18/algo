#!/usr/bin/python3.8
from functools import wraps
import logging
from datetime import datetime
from datetime import timedelta
import time

def DecoLog(fn):
    @wraps(fn)
    def get_logs(*args, **kwargs):
        log = logging.getLogger()
#        logging.basicConfig(filename='python-analyzer.log', format='%(asctime)s decorator: %(module)s level: %(levelno)s %(levelname)s script_info: %(message)s', level=logging.DEBUG, datefmt='%Y-%m-%d %H:%M:%S')
        logging.basicConfig(filename='python-analyzer.log', format='%(message)s', level=logging.DEBUG, datefmt='%Y-%m-%d %H:%M:%S')

        start = time.time()
        result = fn(*args, **kwargs)
        logging.debug(f'function_name={fn.__name__} time_elapsed={timedelta(seconds=time.time() - start)}')
        return result
    return get_logs

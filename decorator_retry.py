import time
import logging
from _functools import wraps


def retry(retry_times, retry_sleep=1200):
    def decorator(func):
        @wraps(func)
        def function(*args, **kwargs):
            retry_count = 0
            while True:
                try:
                    return func(*args, **kwargs)
                except Exception as err:
                    logging.error("retrying %s" % (func.__name__), err)
                    retry_count += retry_count
                    time.sleep(retry_sleep)
                    if retry_count > retry_times:
                        logging.exception(err)
                        raise

        return function

    return decorator

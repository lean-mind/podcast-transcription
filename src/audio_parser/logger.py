import sys
import functools
import logging


def task_logger(_func=None, **kwargs):
    message = kwargs.get("message")
    def log_decorator_info(func):
        @functools.wraps(func)
        def log_decorator_wrapper(*args, **kwargs):
            print(f"START: {message}")
            try:
                func(*args, **kwargs)
                print(f"FINISH: {message}")
            except:
                logging.error(f"Exception: {str(sys.exc_info()[1])}")
                raise
        return log_decorator_wrapper
    return log_decorator_info if _func is None else log_decorator_info(_func)

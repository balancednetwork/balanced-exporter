from loguru import logger
from typing import Callable
from time import sleep


def retry(func: Callable, attempts: int = 0, max_attempts: int = 5, **kwargs):
    if attempts >= max_attempts:
        return None

    try:
        output = func(**kwargs)
        if output is not None:
            return output
        else:
            sleep(1)
            attempts += 1
            retry(func, attempts, **kwargs)
    except Exception as e:
        logger.info(e)
        sleep(1)
        attempts += 1
        retry(func, attempts, **kwargs)

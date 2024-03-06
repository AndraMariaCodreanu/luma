import logging
from typing import Callable

from framework.core import browser


LOG = logging.getLogger(__name__)


def wait_until_is_displayed(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> bool:
        self = args[0]
        if not self.wait_until_is_displayed():
            return False
        return func(*args, **kwargs)

    return wrapper



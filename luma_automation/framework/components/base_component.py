import logging
import time

from framework.core import browser

LOG = logging.getLogger(__name__)


class BaseComponent(object):

    def __init__(self, locator: str = None):
        self._locator = locator

    @property
    def title(self) -> str:
        return browser.get_element_attribute(xpath=self._locator, attribute='title')

    def element_displayed_on_screen(self) -> bool:
        return browser.wait_until_element_is_displayed(locator=self._locator)

    def wait_until_is_displayed(self) -> bool:
        LOG.info(f'Waiting for element with locator "{self._locator}" to be displayed!')
        return browser.wait_until_element_is_displayed(locator=self._locator)

    def wait_until_is_not_displayed(self) -> bool:
        return browser.wait_until_element_is_not_displayed(locator=f"({self._locator})[1]")

    def hover_over(self) -> bool:
        return browser.hover_over(element=self._locator)

    def click(self, scroll: bool = True) -> bool:
        """
        Clicks on element
        :param scroll: Whether to scroll to the element and after that click on it
        :return: bool
        """
        if scroll:
            self.scroll_to()
        return browser.click_on_element_when_available(locator=self._locator)

    def scroll_to(self) -> None:
        """
        Scrolls to element
        :return:
        """
        browser.get_element_location_once_scrolled_into_view(element=self._locator)
        browser.scroll_to(element=self._locator)
        time.sleep(1)


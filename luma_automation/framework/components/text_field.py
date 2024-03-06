from __future__ import absolute_import

from framework.components.base_component import BaseComponent
from framework.core import browser


class TextField(BaseComponent):

    @property
    def text(self) -> str:
        """
        Returns text of element. If the element is not displayed on screen, it waits for it to be
        displayed
        :return: str
        """
        return browser.get_text_from_element(xpath=self._locator, default_value='')

    def wait_until_contains_text(self, value: str, timeout: int = 20) -> bool:
        return browser.wait_until_element_is_displayed(locator=f"{self._locator}[contains(text(), '{value}')]",
                                                       timeout_seconds=timeout)

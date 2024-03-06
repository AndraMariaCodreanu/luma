from framework.components.base_component import BaseComponent
from framework.core import browser


class InputField(BaseComponent):

    def __init__(self, locator: str):
        super().__init__(locator=locator)

    def send_key(self, value: str, wait: int = 2) -> bool:
        return browser.send_key(locator=self._locator, value=value, sleep_after=wait)

    def clear(self) -> None:
        browser.clear_input(locator=self._locator)

    @property
    def text(self) -> str:
        """
        Returns text found in input
        :return:
        """
        return self.get_text()

    @property
    def is_empty(self) -> bool:
        return browser.get_text_from_input(xpath=self._locator) == ''

    def delete_input(self) -> None:
        return browser.delete_input(locator=self._locator)

    def get_text(self) -> str:
        return browser.get_text_from_input(xpath=self._locator)

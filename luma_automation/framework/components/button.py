from framework.components.base_component import BaseComponent
from framework.core import browser


class Button(BaseComponent):

    def __init__(self, locator: str):
        super().__init__(locator=locator)

    def click(self, scroll: bool = True) -> bool:
        """
        Clicks on element
        :param scroll: Whether to scroll to the element and after that click on it
        :return: bool
        """
        return super(Button, self).click(scroll=scroll)

    @property
    def text(self) -> str:
        return browser.get_text_from_element(xpath=self._locator)

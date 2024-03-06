import logging
from typing import List

from framework.components.base_component import BaseComponent
from framework.components.button import Button
from framework.core import browser

LOG = logging.getLogger(__name__)


class DropdownLocators:
    text_locator = "//..//*[contains(text(),'{}')]"
    contains_text_locator = "//*[contains(text(),'{}')]"


class Dropdown(BaseComponent, DropdownLocators):

    def __init__(self, locator: str, dropdown_elements: str):
        super().__init__(locator=locator)
        self.dropdown_elements_locator = dropdown_elements

    @property
    def selected_value(self) -> str:
        return browser.get_text_from_input(xpath=self._locator)

    def get_items(self) -> List[str]:
        return [str(x.text) for x in browser.find_elements(xpath=self.dropdown_elements_locator, timeout_seconds=1)]

    def get_item(self, value: str) -> Button:
        for i, x in enumerate(browser.find_elements(xpath=self.dropdown_elements_locator, timeout_seconds=1)):
            if str(x.text) == value:
                return Button(locator=f"{self.dropdown_elements_locator}[{i + 1}]")

    def wait_dropdown_is_open(self) -> bool:
        return browser.wait_until_element_is_displayed(locator=self.dropdown_elements_locator, multiple=True)

    def wait_dropdown_is_closed(self) -> bool:
        return browser.wait_until_element_is_not_displayed(locator=self.dropdown_elements_locator)

    def is_dropdown_open(self) -> bool:
        return browser.wait_until_element_is_displayed(locator=self.dropdown_elements_locator, timeout_seconds=0,
                                                       multiple=True)

    def select(self, value: str) -> bool:
        self.wait_dropdown_is_open()
        LOG.info(f"Element to select {self.dropdown_elements_locator}{self.text_locator.format(value)}")
        result = browser.click_on_element_when_available(
            locator=f"{self.dropdown_elements_locator}{self.text_locator.format(value)}")
        return result

    def hover_and_select(self, value: str) -> bool:
        self.wait_dropdown_is_open()
        LOG.info(f"Element to select {self.dropdown_elements_locator}{self.text_locator.format(value)}")
        result = browser.hover_over(
            element=f"{self.dropdown_elements_locator}{self.text_locator.format(value)}")
        return result

    def select_contains_value(self, value: str) -> bool:
        self.wait_dropdown_is_open()
        LOG.info(f"Element to select {self.dropdown_elements_locator}{self.contains_text_locator.format(value)}")
        result = browser.click_on_element_when_available(
            locator=f"{self.dropdown_elements_locator}{self.contains_text_locator.format(value)}")
        return result

    def click_and_select_contains_value(self, value: str) -> bool:
        if self.selected_value is None:
            LOG.info(f'Searched value to compare is {self.selected_value} !')
            pass
        elif value in self.selected_value:
            return True
        return self.click() and self.select_contains_value(value=value)

    def click_and_select(self, value: str) -> bool:
        if self.selected_value == value:
            return True
        return self.click() and self.select(value=value)

    def click_hover_and_select(self, value: str) -> bool:
        if self.selected_value == value:
            return True
        return self.click() and self.hover_and_select(value=value)

    def value_in_dropdown(self, value: str) -> bool:
        return browser.wait_until_element_is_displayed(
            locator=f"{self.dropdown_elements_locator}{self.text_locator.format(value)}",
            timeout_seconds=0)

    def hover_over_selected_value(self) -> bool:
        return browser.hover_over(element=self._locator)

from framework.components import base_component
from framework.core import browser


class SwatchLocators:
    size_locator = '//div[@aria-label="{}"]'
    size_list_locator = '//div[@class="swatch-option text"]'
    color_locator = '//div[@option-label="{}"]'
    color_list_locator = '//div[@class="swatch-option color"]'


class Swatch(SwatchLocators, base_component.BaseComponent):

    def select_size(self, size=None):
        if size:
            return browser.click_on_element(locator=self.size_locator.format(size))
        else:
            return browser.click_on_element(
                locator=self.size_locator.format(self.get_available_size_for_the_product()[1]))

    def get_available_size_for_the_product(self):
        size_elements = browser.find_elements(xpath=self.size_list_locator)
        size = []
        for index in range(1, len(size_elements)):
            color_found = browser.get_element_attribute(xpath=f'{self.size_list_locator}[{index}]',
                                                        attribute="aria-label")
            size.append(color_found)
        print(size)
        return size

    def select_color(self, color=None):
        if color:
            return browser.click_on_element(locator=self.color_locator.format(color))
        else:
            return browser.click_on_element(
                locator=self.color_locator.format(self.get_available_colors_for_the_product()[0]))

    def get_available_colors_for_the_product(self):
        color_elements = browser.find_elements(xpath=self.color_list_locator)
        colors = []
        for index in range(1, len(color_elements)):
            color_found = browser.get_element_attribute(xpath=f'{self.color_list_locator}[{index}]',
                                                        attribute="option-label")
            colors.append(color_found)
            print(color_found)
        print(colors)
        return colors

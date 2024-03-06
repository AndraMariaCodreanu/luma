from framework.components import button, text_field, base_component
from framework.core import browser


class FilterBlockLocators:
    current_filters_locator = '//div[@class="filter-current"]'
    subtitle_locator = '//strong[contains(@class,"subtitle filter-current")] '
    clear_all_locator = '//a[@class="action clear filter-clear"]'


class FilterBlock(FilterBlockLocators, base_component.BaseComponent):
    def __init__(self):
        super().__init__()
        self.filter_subtitle = text_field.TextField(locator=self.subtitle_locator)
        self.filter_content = CurrentFilter(locator=self.current_filters_locator)
        self.clear_all_action = button.Button(locator=self.clear_all_locator)

    @property
    def current_filters(self):
        elements_locator = f'{self._locator}{self.current_filters_locator}'
        elements_count = browser.count_elements(xpath=elements_locator)
        return [CurrentFilter(f"({elements_locator})[{element_index}]") for element_index in
                range(1, elements_count + 1)]


class CurrentFilterLocators:
    filter_label_locator = '//span[@class="filter-label"]'
    filter_value_locator = '//span[@class="filter-value"]'
    remove_filter_locator = '//a[@class="action remove"]'


class CurrentFilter(base_component.BaseComponent, CurrentFilterLocators):

    def __init__(self, locator):
        super().__init__(locator=locator)
        self.filter_label = text_field.TextField(locator=f'{self._locator}{self.filter_label_locator}')
        self.filter_value = text_field.TextField(locator=f'{self._locator}{self.filter_value_locator}', )
        self.remove_filter = button.Button(locator=f'{self._locator}{self.remove_filter_locator}')

from framework.components import text_field, dropdown, button, filter_block
from framework.components.base_component import BaseComponent
from framework.core import browser


class SideBarLocators():
    subtitle_locator = '//strong[@role="heading"]'
    associated_options_items_locator = '//div[contains(@class,"filter-options-item")]'
    shop_by_tops_category_locator = "//a[text()='Tops']"
    shop_by_bottoms_category_locator = "//a[text()='Bottoms']"
    shop_by_bags_locator = ''# todo- not implemented
    shop_by_fitness_quipment_locator = ''# todo- not implemented
    shop_by_watches_locator = ''# todo- not implemented
    shop_by_video_download_locator = ''# todo- not implemented
    filter_locator = '//div[@class="filter-current" and @data-collapsible="true"]'


class SideBar(SideBarLocators, BaseComponent):
    def __init__(self, locator):
        super().__init__(locator=locator)
        self.subtitle = text_field.TextField(locator=f'{self._locator}{self.subtitle_locator}')
        self.tops_category = button.Button(locator=self.shop_by_tops_category_locator)
        self.bottoms_category = button.Button(locator=self.shop_by_bottoms_category_locator)
        self.bags_category = button.Button(locator=self.shop_by_bags_locator)
        self.fitness_equipment_category = button.Button(locator=self.shop_by_fitness_quipment_locator)
        self.watches_category = button.Button(locator=self.shop_by_watches_locator)
        self.video_category = button.Button(locator=self.shop_by_video_download_locator)
        self.associated_option = AssociatedOptionItem(locator=self.associated_options_items_locator)
        self.shopping_by_filter = filter_block.FilterBlock()
        self.compare_products = CompareProducts()
        self.my_wish_list = MyWishList()

    @property
    def associated_options(self):
        elements_locator = f'{self._locator}{self.associated_options_items_locator}'
        elements_count = browser.count_elements(xpath=elements_locator)
        return [AssociatedOptionItem(f"({elements_locator})[{element_index}]") for element_index in
                range(1, elements_count + 1)]


class AssociatedOptionItemLocators:
    item_option_dropdown_locator = "//div[contains(@class,filter-options-title')]"
    item_option_dropdown_elements_locator = "//..//div[@class='filter-options-content']/ol/li"


class AssociatedOptionItem(AssociatedOptionItemLocators, BaseComponent):
    def __init__(self, locator):
        super().__init__(locator=locator)
        self.option_name = button.Button(locator=f'{self._locator}{self.item_option_dropdown_locator}')
        self.option = dropdown.Dropdown(locator=f'{self._locator}{self.item_option_dropdown_locator}',
                                        dropdown_elements=self.item_option_dropdown_elements_locator)


class CompareProductsLocators:
    # todo- not implemented
    pass


class CompareProducts(CompareProductsLocators):
    def __init__(self):
        super().__init__()
    # todo- not implemented


class MyWishListLocators:
    # todo- not implemented
    pass


class MyWishList(MyWishListLocators):
    def __init__(self):
        super().__init__()
    # todo- not implemented

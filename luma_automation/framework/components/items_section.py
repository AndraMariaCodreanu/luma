from framework.components import text_field, button, dropdown, reviews, swatch, input_field, base_component
from framework.core import browser


class ItemsSectionLocators:
    mode_locator = '//div[@class="modes"]'
    sort_by_dropdown_locator = '//select[@data-role="sorter"]'
    sort_by_elements_locator = '//option'
    direction_locator = '//a[@data-role="direction-switcher"]'
    product_locator = '//li[contains(@class,"product-item")]'


class ItemsSection(ItemsSectionLocators, base_component.BaseComponent):
    def __init__(self, locator):
        super().__init__(locator=locator)
        self.mode = Mode(locator=self.mode_locator)
        self.sort_by = dropdown.Dropdown(locator=self.sort_by_dropdown_locator,
                                         dropdown_elements=self.sort_by_elements_locator)
        self.set_direction = button.Button(locator=self.direction_locator)
        self.product = Product(locator=self.product_locator)
        # self.pages = pages
        # self.limit_items_per_page = dropdown

    @property
    def associated_products(self):
        elements_locator = f'{self._locator}{self.product_locator}'
        elements_count = browser.count_elements(elements_locator)
        return [Product(f"({elements_locator})[{element_index}]") for element_index in
                range(1, elements_count + 1)]


class ProductLocators:
    product_name_locator = '//strong[contains(@class,"product-item-name")]'
    product_reviews_locator = '//div[contains(@class,"product-reviews-summary")]'
    product_price_locator = '//div[contains(@class,"price-box")]'
    product_swatch_locator = '//div[contains(@data-role,"swatch-option")]'
    product_add_to_cart_locator = '//button[contains(@class,"tocart")]'
    product_add_to_wish_list_locator = '//a[@data-action="add-to-wishlist"]'
    product_add_to_compare_locator = '//a[@class="action tocompare"]'
    qty_input_locator = '//input[@id="qty"]'


class Product(ProductLocators, base_component.BaseComponent):
    def __init__(self, locator):
        super().__init__(locator=locator)
        self.product_name = text_field.TextField(locator=f'{self._locator}{self.product_name_locator}')
        self.reviews = reviews.Reviews(locator=f'{self._locator}{self.product_reviews_locator}')
        self.price = text_field.TextField(locator=f'{self._locator}{self.product_price_locator}')
        self.swatch = swatch.Swatch(locator=f'{self._locator}{self.product_swatch_locator}')
        self.add_to_cart = button.Button(locator=f'{self._locator}{self.product_add_to_cart_locator}')
        self.add_to_wish_list = button.Button(locator=f'{self._locator}{self.product_add_to_wish_list_locator}')
        self.add_to_compare = button.Button(locator=f'{self._locator}{self.product_add_to_compare_locator}')
        self.qty = input_field.InputField(locator=self.qty_input_locator)


class ModesLocators:
    grid_mode_active_locator = '//strong[@data-value="grid"]'
    list_mode_active_locator = '//strong[@data-value="list"]'
    grid_mode_inactive_locator = '//a[@data-value="grid"]'
    list_mode_inactive_locator = '//a[@data-value="list"]'


class Mode(ModesLocators, base_component.BaseComponent):
    def __init__(self, locator):
        super().__init__(locator=locator)
        self.grid_mode_active = button.Button(f'{self._locator}{self.grid_mode_active_locator}')
        self.list_mode_active = button.Button(f'{self._locator}{self.list_mode_active_locator}')
        self.grid_mode_inactive = button.Button(f'{self._locator}{self.grid_mode_inactive_locator}')
        self.list_mode_inactive = button.Button(f'{self._locator}{self.list_mode_inactive_locator}')

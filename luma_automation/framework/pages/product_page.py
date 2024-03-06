from framework.components import text_field, button, header
from framework.components.items_section import Product


class ProductLocators:
    page_title_locator = '//h1[@class="page-title"]'
    product_info_locator = '//div[@class="product-info-main"]'
    related_products_locator = '//li[@class="item product product-item"]'
    header_locator = "//header[@class='page-header']"
    navigation_locator = '//div[contains(@class,"nav-sections-items")]'
    alert_message_locator = '//div[@role="alert"]'
    succes_message_locator = '//div[@role="alert"]//a[text()="shopping cart"]'


class ProductPage(ProductLocators):
    def __init__(self):
        super().__init__()
        self.header = header.Header(locator=self.header_locator)
        self.page_title = text_field.TextField(locator=self.page_title_locator)
        self.product = Product(locator=self.product_info_locator)
        self.related_products = Product(locator=self.related_products_locator)
        self.go_to_cart = button.Button(locator=self.succes_message_locator)

    def enter_product_details_and_add_to_cart(self):
        self.product.swatch.select_size()
        self.product.swatch.select_color()
        self.product.qty.send_key(value="1")
        self.product.add_to_cart.click()
        self.go_to_cart.click()

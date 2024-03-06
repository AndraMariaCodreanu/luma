from framework.components import text_field, table, button, base_component


class ShoppingCartLocators:
    page_title_locator = ''
    cart_table_locator = '//table[@id="shopping-cart-table"]'
    cart_summary_locator = '//table[@class="data table totals"]'


class ShoppingCart(ShoppingCartLocators, base_component.BaseComponent):
    def __init__(self):
        super().__init__()
        self.page_title = text_field.TextField(locator=self.page_title_locator)
        self.cart_table = table.Table(locator=self.cart_table_locator)
        self.cart_summary = ShoppingCartSummary(locator=self.cart_summary_locator)

    def get_items_from_cart_from_row(self, row_number):
        headers = self.cart_table.header
        content = []
        for header in headers:
            print(f'for header : {header}')
            items = self.cart_table.get_cell_content_from_row_under_column(row_index=row_number, column_name=header)
            content.append(items)
        return content


class ShoppingCartSummaryLocators:
    title_locator = '//strong[@class="summary title"]'
    cart_summary_table_locator = '//table[@class="data table totals"]'
    proceed_to_checkout_locator = '//button[@data-role="proceed-to-checkout"]'


class ShoppingCartSummary(ShoppingCartSummaryLocators, base_component.BaseComponent):
    def __init__(self, locator):
        super().__init__(locator=locator)
        self.summary_title = text_field.TextField(locator=self.title_locator)
        self.summary_table = table.Table(locator=self.cart_summary_table_locator)
        self.proceed_to_checkout = button.Button(locator=self.proceed_to_checkout_locator)

    def get_subtotal(self):
        pass

    def get_discount(self):
        pass

    def get_shipping_price(self):
        pass

    def get_order_total(self):
        pass

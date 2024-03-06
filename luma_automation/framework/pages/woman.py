from framework.components import header, navigation_bar, text_field, side_bar_menu, items_section


class WomanLocators:
    header_locator = "//header[@class='page-header']"
    navigation_locator = '//div[contains(@class,"nav-sections-items")]'
    page_title_locator = '//h1[@class="page-title"]'
    side_bar_locator = '//div[@class="sidebar sidebar-main"]'
    product_locator = '//ol[contains(@class,"product-items")]'


class WomanConstants:
    tees_category = "Tees"


class WomanPage(WomanLocators, WomanConstants):
    def __init__(self):
        super().__init__()
        self.header = header.Header(locator=self.header_locator)
        self.navigation = navigation_bar.NavigationBar(locator=self.navigation_locator)
        # self.breadcrumbs = breadcrumbs
        self.page_title = text_field.TextField(locator=self.page_title_locator)
        self.side_bar = side_bar_menu.SideBar(locator=self.side_bar_locator)
        self.items = items_section.ItemsSection(locator=self.product_locator)
        # self.footer = footer

    def select_tees_category_and_select_one_item(self):
        self.side_bar.associated_options[0].click()
        self.side_bar.associated_options[0].option.select(value=self.tees_category)
        assert self.items.wait_until_is_displayed(), 'FAIL, Items are not displayed after filtr'
        self.items.associated_products[0].product_name.click()
        print(f'Selected item is {self.items.associated_products[0].product_name.text}')

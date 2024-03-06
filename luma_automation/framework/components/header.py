from framework.components import button, input_field, navigation_bar, base_component


class HeaderLocators:
    sign_in_button_locator = "//li[@class='authorization-link']/a[contains(@href,'login')]"
    create_account_button_locator = "//a[contains(@href,'create')]"
    search_bar_locator = ""
    menu_bar_locator = "//div[@class='sections nav-sections']"
    # shopping_cart_locator = ""


class Header(HeaderLocators, base_component.BaseComponent):
    def __init__(self, locator):
        super().__init__(locator=locator)
        self.sign_in = button.Button(locator=f'{self._locator}{self.sign_in_button_locator}')
        self.create_account = button.Button(locator=f'{self._locator}{self.create_account_button_locator}')
        self.search_bar = input_field.InputField(locator=f'{self._locator}{self.search_bar_locator}')
        self.navigation = navigation_bar.NavigationBar(locator=f'{self.menu_bar_locator}')
        # self.shopping_cart_icon = base_component.BaseComponent(locator=f'{self._locator}{self.shopping_cart_locator}')
        #todo need to implemnt cart icon functionality
from framework.components import button, base_component


class NavigationLocators:
    whats_new_locator = "//a[contains(@href,'what-is-new')]"
    woman_locator = "//a[contains(@class,'level-top') and contains(@href,'women')]"


class NavigationBar(NavigationLocators, base_component.BaseComponent):
    def __init__(self, locator: str):
        super().__init__(locator=locator)
        self.whats_new_option = button.Button(locator=f'{self._locator}{self.whats_new_locator}')
        self.woman_option = button.Button(locator=self.woman_locator)
        # self.men_option = dropdown.Dropdown(self.men_locator) todo- not implemented
        # self.gear_option = dropdown.Dropdown(self.gear_locator)todo- not implemented
        # self.training_option = dropdown.Dropdown(self.training_locator)todo- not implemented
        # self.sale_option = button.Button(self.sale_locator)todo- not implemented

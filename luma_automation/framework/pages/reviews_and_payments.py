from framework.components import base_component, button


class ReviewAndPaymentsLocators:
    place_order_button_locator = '//button[@class="action primary checkout"]'


class ReviewAndPaymentsPage(base_component.BaseComponent, ReviewAndPaymentsLocators):
    def __init__(self):
        super().__init__()
        self.place_order = button.Button(locator=self.place_order_button_locator)

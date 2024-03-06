from framework.components import base_component, button


class ShingingAddressLocators:
    next_button_locator = '//button[@data-role="opc-continue"]'


class ShippingAddressPage(base_component.BaseComponent, ShingingAddressLocators):
    def __init__(self):
        super().__init__()
        self.next = button.Button(locator=self.next_button_locator)

from framework.components import base_component, button, text_field


class ConfirmationLocators:
    continue_button_locator = '//a[@class="action primary continue"]'
    page_title_locator = '//h1[@class="page-title"]'
    confirmation_text_locator = '//div[@class="checkout-success"]//p'


class ConfirmationPage(base_component.BaseComponent, ConfirmationLocators):
    def __init__(self):
        super().__init__()
        self.page_title = text_field.TextField(locator=self.page_title_locator)
        self.continue_shopping = button.Button(locator=self.continue_button_locator)
        self.confirmation_content = text_field.TextField(locator=self.confirmation_text_locator)

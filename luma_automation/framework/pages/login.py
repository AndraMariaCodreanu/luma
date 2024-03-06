import logging

from framework.components import text_field, input_field, button

logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger(__name__)


class LoginLocators():
    page_title_locator = "//h1[@class='page-title']"
    email_locator = "//input[@id='email']"
    password_locator = "//input[@id='pass']"
    sign_in_locator = "//button[@class='action login primary']"
    forgot_pwd_locator = "//a[@class='action remind']"
    create_account_locator = "//a[@class='action create primary']"
    welcome_user_message_locator = "//li[@class='greet welcome']/span[@class='logged-in']"
    customer_menu_options_locator = "//li[@class='customer-welcome']"
    customer_menu_dropdown_elements = "//ul/li"


class LoginPage(LoginLocators):
    def __init__(self):
        super().__init__()
        self.page_title = text_field.TextField(locator=self.page_title_locator)
        self.email = input_field.InputField(locator=self.email_locator)
        self.password = input_field.InputField(locator=self.password_locator)
        self.sign_in = button.Button(locator=self.sign_in_locator)
        self.forgot_password = button.Button(locator=self.forgot_pwd_locator)
        self.create_account = button.Button(locator=self.create_account_locator)

    def perform_login(self, username="andra.maria.codreanu@gmail.com", pasword="1234P@ss"):
        LOG.info("Trying to perform login . . . ")
        self.email.wait_until_is_displayed()
        self.email.send_key(value=username)
        self.password.wait_until_is_displayed()
        self.password.send_key(value=pasword)
        self.sign_in.wait_until_is_displayed()
        self.sign_in.click()
        self.sign_in.wait_until_is_not_displayed()

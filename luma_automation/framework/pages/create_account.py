from framework.components import input_field, button


class CreateAccountLocators:
    first_name_input_locator = "//input[@id='firstname']"
    last_name_input_locator = "//input[@id='lastname']"
    email_input_locator = "//input[@id='email_address']"
    password_input_locator = "//input[@id='password']"
    confirm_password_input_locator = "//input[@id='password-confirmation']"
    create_account_button_locator = "//button[@title='Create an Account']"


class CreateAccount(CreateAccountLocators):
    def __init__(self):
        super().__init__()
        self.first_name = input_field.InputField(locator=self.first_name_input_locator)
        self.last_name = input_field.InputField(locator=self.last_name_input_locator)
        self.email = input_field.InputField(locator=self.email_input_locator)
        self.password = input_field.InputField(locator=self.password_input_locator)
        self.confirm_password = input_field.InputField(locator=self.confirm_password_input_locator)
        self.create_account_button = button.Button(locator=self.create_account_button_locator)

    def create_account(self, first_name, last_name, email, password):
        self.first_name.send_key(first_name)
        self.last_name.send_key(last_name)
        self.email.send_key(email)
        self.password.send_key(password)
        self.confirm_password.send_key(password)
        self.create_account_button.click()
        self.create_account_button.wait_until_is_not_displayed()

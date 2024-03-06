from framework.components import header
from framework.pages import login, create_account, logout


class LandingPageLocators:
    header_locator = "//header[@class='page-header']"


class LandingPage(LandingPageLocators):

    def __init__(self):
        super().__init__()
        self.header = header.Header(locator=self.header_locator)
        self.login_option = login.LoginPage()
        self.create_account_option = create_account.CreateAccount()
        self.logout_option = logout.LogoutPage()

    def perform_login(self, username="andra.maria.codreanu@gmail.com", password="1234P@ss"):
        self.header.sign_in.click()
        self.login_option.perform_login(username=username, pasword=password)

    def create_account(self, first_name, last_name, email, password):
        self.header.create_account.click()
        self.create_account_option.create_account(first_name=first_name, last_name=last_name, email=email,
                                                  password=password)

    def perform_logout(self):
        self.logout_option.perform_logout()

    def navigate_to_woman_page(self):
        self.header.navigation.woman_option.click()

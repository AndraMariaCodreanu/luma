from framework.components import dropdown
import logging

logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger(__name__)


class LogoutConstants:
    user_button_locator = "//li[@class='customer-welcome']"
    user_button_elements_locator = "//ul/li"


class LogoutLocators:
    log_out = "Sign Out"


class LogoutPage(LogoutConstants, LogoutLocators):
    def __init__(self):
        super().__init__()
        self.user_action = dropdown.Dropdown(locator=self.user_button_locator,
                                             dropdown_elements=self.user_button_elements_locator)

    def perform_logout(self):
        LOG.info("Trying to perform logout ...")
        self.user_action.click_and_select_contains_value(value=self.log_out)

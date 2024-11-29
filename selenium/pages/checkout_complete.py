from .base import BasePage
from .locators import CheckoutCompleteLocators


class CheckoutCompletePage(BasePage):
    def get_message(self):
        return self.driver.find_element(*CheckoutCompleteLocators.MESSAGE_HEADER).text

from .base import BasePage
from .locators import CheckoutStepTwoLocators


class CheckoutStepTwoPage(BasePage):
    def finish_order(self):
        self.driver.find_element(*CheckoutStepTwoLocators.FINISH_BUTTON).click()

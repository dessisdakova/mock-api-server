from .base import BasePage
from .locators import CheckoutStepTwoLocators


class CheckoutStepTwoPage(BasePage):
    def get_items_count_in_order(self):
        return len(self.driver.find_elements(*CheckoutStepTwoLocators.ITEMS_IN_ORDER))


    def finish_order(self):
        self.driver.find_element(*CheckoutStepTwoLocators.FINISH_BUTTON).click()

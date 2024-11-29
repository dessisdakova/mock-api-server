from .base import BasePage
from .locators import CheckoutStepOneLocators


class CheckoutStepOnePage(BasePage):
    def enter_information(self, first_name, last_name, zip_code):
        self.driver.find_element(*CheckoutStepOneLocators.FIRST_NAME_FIELD).send_keys(first_name)
        self.driver.find_element(*CheckoutStepOneLocators.LAST_NAME_FIELD).send_keys(last_name)
        self.driver.find_element(*CheckoutStepOneLocators.ZIP_CODE_FIELD).send_keys(zip_code)

    def click_continue_button(self):
        self.driver.find_element(*CheckoutStepOneLocators.CONTINUE_BUTTON).click()

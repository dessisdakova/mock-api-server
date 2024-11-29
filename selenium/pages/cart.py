from .base import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    def get_items_count_in_cart(self):
        return len(self.driver.find_elements(*CartPageLocators.ITEMS_IN_CART))

    def click_checkout(self):
        self.driver.find_element(*CartPageLocators.CHECKOUT_BUTTON).click()

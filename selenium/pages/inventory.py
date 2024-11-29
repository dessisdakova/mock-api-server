from .locators import InventoryPageLocators
from .base import BasePage


class InventoryPage(BasePage):
    def add_item_to_cart(self):
        self.driver.find_element(*InventoryPageLocators.ADD_BACKPACK_BUTTON).click()

    def go_to_cart(self):
        self.driver.find_element(*InventoryPageLocators.SOPPING_CART_LINK).click()

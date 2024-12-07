import json
from pathlib import Path
import pytest
from pages import *


def load_input_data():
    file_path = Path(__file__).resolve().parent / "input_data.json"
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


@pytest.mark.parametrize("input_data", load_input_data())
def test_automate_steps_and_assert_message(driver, input_data):
    login_page = LoginPage(driver)
    login_page.load(LoginPageLocators.BASE_URL, LoginPageLocators.LOGO_DIV)
    assert "www.saucedemo.com" in driver.current_url, "Site not loaded."
    login_page.enter_credentials(input_data["username"], input_data["password"])
    assert driver.find_element(*LoginPageLocators.USERNAME_FIELD).get_attribute("value") == input_data["username"]
    assert driver.find_element(*LoginPageLocators.PASSWORD_FIELD).get_attribute("value") == input_data["password"]
    login_page.click_login_button()

    inventory_page = InventoryPage(driver)
    inventory_page.load(InventoryPageLocators.BASE_URL, InventoryPageLocators.INVENTORY_CONTAINER)
    assert "inventory" in driver.current_url, "Inventory page not loaded."
    inventory_page.add_item_to_cart()
    inventory_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.load(CartPageLocators.BASE_URL, CartPageLocators.CART_CONTENTS_CONTAINER)
    assert "cart" in driver.current_url, "Cart page not loaded."
    assert cart_page.get_items_count_in_cart() == 1, "Item was not added to cart."
    cart_page.click_checkout()

    checkout_one_page = CheckoutStepOnePage(driver)
    checkout_one_page.load(CheckoutStepOneLocators.BASE_URL, CheckoutStepOneLocators.CHECKOUT_INFO_CONTAINER)
    assert "checkout-step-one" in driver.current_url, "Checkout-step-one page not loaded."
    checkout_one_page.enter_information(input_data["first_name"], input_data["last_name"], input_data["postal_code"])
    assert driver.find_element(*CheckoutStepOneLocators.FIRST_NAME_FIELD).get_attribute("value") == input_data["first_name"]
    assert driver.find_element(*CheckoutStepOneLocators.LAST_NAME_FIELD).get_attribute("value") == input_data["last_name"]
    assert driver.find_element(*CheckoutStepOneLocators.ZIP_CODE_FIELD).get_attribute("value") == input_data["postal_code"]
    checkout_one_page.click_continue_button()

    checkout_two_page = CheckoutStepTwoPage(driver)
    checkout_two_page.load(CheckoutStepTwoLocators.BASE_URL, CheckoutStepTwoLocators.SUMMARY_INFO_DIV)
    assert "checkout-step-two" in driver.current_url, "Checkout-step-two page not loaded."
    assert checkout_two_page.get_items_count_in_order() == 1, "Item was not added to order."
    checkout_two_page.finish_order()

    checkout_complete_page = CheckoutCompletePage(driver)
    checkout_complete_page.load(CheckoutCompleteLocators.BASE_URL, CheckoutCompleteLocators.CHECKOUT_COMPLETE_CONTAINER)
    assert checkout_complete_page.get_message() == "Thank you for your order!", "Order was not complete."

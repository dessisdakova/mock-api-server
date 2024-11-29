from selenium.webdriver.common.by import By


class LoginPageLocators:
    BASE_URL = "https://www.saucedemo.com"
    USERNAME_FIELD = (By.CSS_SELECTOR, "input[data-test='username']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input[data-test='password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input[data-test='login-button']")
    LOGO_DIV = (By.CLASS_NAME, "login_logo")  # for explicit wait


class InventoryPageLocators:
    BASE_URL = "https://www.saucedemo.com/inventory.html"
    SOPPING_CART_LINK = (By.CSS_SELECTOR, "a[data-test='shopping-cart-link']")
    ADD_BACKPACK_BUTTON = (By.CSS_SELECTOR, "button[data-test='add-to-cart-sauce-labs-backpack']")
    INVENTORY_CONTAINER = (By.ID, "inventory_container")  # for explicit wait


class CartPageLocators:
    BASE_URL = "https://www.saucedemo.com/cart.html"
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "button[data-test='checkout']")
    ITEMS_IN_CART = (By.CSS_SELECTOR, "div[data-test='inventory-item-name']")
    CART_CONTENTS_CONTAINER = (By.ID, "cart_contents_container")  # for explicit wait


class CheckoutStepOneLocators:
    BASE_URL = "https://www.saucedemo.com/checkout-step-one.html"
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, "input[data-test='firstName']")
    LAST_NAME_FIELD = (By.CSS_SELECTOR, "input[data-test='lastName']")
    ZIP_CODE_FIELD = (By.CSS_SELECTOR, "input[data-test='postalCode']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "input[data-test='continue']")
    CHECKOUT_INFO_CONTAINER = (By.ID, "checkout_info_container")  # for explicit wait


class CheckoutStepTwoLocators:
    BASE_URL = "https://www.saucedemo.com/checkout-step-two.html"
    FINISH_BUTTON = (By.CSS_SELECTOR, "button[data-test='finish']")
    SUMMARY_INFO_DIV = (By.CLASS_NAME, "summary_info")  # for explicit wait


class CheckoutCompleteLocators:
    BASE_URL = "https://www.saucedemo.com/checkout-complete.html"
    MESSAGE_HEADER = (By.CSS_SELECTOR, "h2[data-test='complete-header']")
    CHECKOUT_COMPLETE_CONTAINER = (By.ID, "checkout_complete_container")  # for explicit wait



from .base import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def enter_credentials(self, username: str, password: str):
        self.driver.find_element(*LoginPageLocators.USERNAME_FIELD).send_keys(username)
        self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def load(self, url, wait_for_locator=None, timeout=5):
        self.driver.get(url)
        if wait_for_locator:
            WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located(wait_for_locator))

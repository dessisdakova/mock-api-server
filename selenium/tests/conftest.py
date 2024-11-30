import json
from pathlib import Path
import pytest
from typing import Generator
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.edge.options import Options


@pytest.fixture(scope="session")
def config():
    current_dir = Path(__file__).resolve().parent
    config_path = current_dir / "config.json"
    with open(config_path) as file:
        data = json.load(file)
    return data


@pytest.fixture(scope="session")
def driver(config) -> Generator[webdriver.Remote, None, None]:
    browser = config["browser"].lower()
    wait_time = config["wait_time"]

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    if browser == "chrome":
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        driver = webdriver.Firefox(options=options)
    elif browser == "edge":
        driver = webdriver.Edge(options=options)
    else:
        raise ValueError(f"Unsupported browser: '{browser}'")

    driver.implicitly_wait(wait_time)
    yield driver
    driver.quit()

    """
    # Using Sauce Labs configuration to run tests on browsers across different operating systems
    sauce_url = f"https://{sauce_username}:{sauce_access_key}@ondemand.eu-central-1.saucelabs.com:443/wd/hub"
    options = Options()
    options.set_capability("browserName", "safari")  # Example: Replace "chrome" with your desired browser
    options.set_capability("platformName", "macOS 13")
    options.set_capability("browserVersion", "latest")
    driver = Remote(command_executor=sauce_url, options=options)
    """

import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver: WebDriver, url: str):
        self.driver = driver
        self.url = url

    def open_url(self):
        self.driver.get(self.url)

    def wait_until_element_be_clickable(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable(locator))

    @staticmethod
    def sleep_during_specific_time(timeout=10):
        return time.sleep(timeout)

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Constants:
    URL: str = "http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html"


class Locators:
    DRAG_ACTION = (By.XPATH, '//*[@id="box3"]')
    DPOP_ACTION = (By.XPATH, '//*[@id="box103"]')


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_url(self, url: str):
        self.driver.get(url)

    def drag_and_drop_operations(self, locators: Locators):
        drag = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(locators.DRAG_ACTION))
        drop = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(locators.DPOP_ACTION))
        return ActionChains(self.driver).drag_and_drop(drag, drop).perform()


if __name__ == "__main__":
    page = BasePage(driver=webdriver.Chrome())
    page.get_url(Constants.URL)
    page.drag_and_drop_operations(Locators())

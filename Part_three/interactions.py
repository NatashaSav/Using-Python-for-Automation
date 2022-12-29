import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Constants:
    URL: str = 'https://www.google.com/earth/'
    SHADOW_ROOT: str = 'return arguments[0].shadowRoot'


class Locators:
    EARTH_APP = (By.CSS_SELECTOR, "body > earth-app")
    TOOLBAR = (By.CSS_SELECTOR, '#toolbar')
    MENU_BTN = (By.CSS_SELECTOR, '#menu')


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_url(self, url: str):
        self.driver.get(url)

    def click_menu_btn(self):
        wait = WebDriverWait(self.driver, 60)
        time.sleep(10)
        earth_app = self.driver.find_element(*Locators.EARTH_APP)
        shadow_earth_app = self.driver.execute_script(Constants.SHADOW_ROOT, earth_app)

        toolbar = shadow_earth_app.find_element(*Locators.TOOLBAR)
        toolbar_shadow = self.driver.execute_script(Constants.SHADOW_ROOT, toolbar)

        menu_btn = toolbar_shadow.find_element(*Locators.MENU_BTN)
        launch_menu_btn = wait.until(EC.element_to_be_clickable(menu_btn))
        launch_menu_btn.click()


if __name__ == "__main__":
    page = BasePage(driver=webdriver.Chrome())
    page.get_url(Constants.URL)
    page.click_menu_btn()

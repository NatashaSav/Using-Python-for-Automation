from selenium.webdriver.common.by import By


class Locators:
    EARTH_APP = (By.CSS_SELECTOR, "body > earth-app")
    TOOLBAR = (By.CSS_SELECTOR, '#toolbar')
    MENU_BTN = (By.CSS_SELECTOR, '#menu')
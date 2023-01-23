from selenium.webdriver.common.by import By


class Locators:
    LIST_OF_CAPITALS = (By.XPATH, '//*[@id="dropContent"]')
    LIST_OF_COUNTRIES = (By.XPATH, '//*[@id="countries"]')
    DRAG_ACTION = (By.XPATH, '//*[@id="box3"]')
    DROP_ACTION = (By.XPATH, '//*[@id="box103"]')
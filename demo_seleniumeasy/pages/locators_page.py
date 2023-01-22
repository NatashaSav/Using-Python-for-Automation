from selenium.webdriver.common.by import By


class Locators:
    USER_MSG = (By.XPATH, '//*[@id="user-message"]')
    DISPLAYED_TEXT = (By.XPATH, '//*[@id="display"]')
    DISPLAYED_TOTAL_VALUE = (By.XPATH, '//*[@id="displayvalue"]')
    SHOW_MSG_BTN = (By.XPATH, '//*[@id="get-input"]/button')
    FIRST_FIELD = (By.XPATH, '//*[@id="sum1"]')
    SECOND_FIELD = (By.XPATH, '//*[@id="sum2"]')
    GET_TOTAL_BTN = (By.XPATH, '//*[@id="gettotal"]/button')

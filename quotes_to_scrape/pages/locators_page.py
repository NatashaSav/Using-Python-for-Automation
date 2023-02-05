from selenium.webdriver.common.by import By


class Locators:
    LOGIN_BTN = (By.XPATH, '/html/body/div/div[1]/div[2]/p/a')
    USERNAME_FIELD = (By.XPATH, '//*[@id="username"]')
    PASSWORD_FIELD = (By.XPATH, '//*[@id="password"]')
    LOGIN_AS_AUTHORISED_USER = (By.XPATH, '/html/body/div/form/input[2]')
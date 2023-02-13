from selenium.webdriver.common.by import By


class Locators:
    LOGIN_BTN = (By.XPATH, '//a[@href="/login"]')
    USERNAME_FIELD = (By.XPATH, '//*[@id="username"]')
    PASSWORD_FIELD = (By.XPATH, '//*[@id="password"]')
    LOGIN_AS_AUTHORISED_USER = (By.XPATH, '/html/body/div/form/input[2]')
    # LOGIN_AS_AUTHORISED_USER = (By.CLASS_NAME, 'btn.btn-primary')
    # LOGIN_AS_AUTHORISED_USER = (By.XPATH, '//input[type="submit"]')
    # LOGIN_AS_AUTHORISED_USER = (By.XPATH, '//input[value="Login"]')
    # LOGIN_AS_AUTHORISED_USER = (By.XPATH, 'form/input[type="submit"]')

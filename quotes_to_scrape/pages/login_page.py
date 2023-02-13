import time

from quotes_to_scrape.pages.locators_page import Locators


class Credentials:
    USERNAME = "Natalia91"
    PASSWORD = "434708"


class Login:
    def __init__(self, browser):
        self.browser = browser

    def click_login(self):
        return self.browser.find_element(*Locators.LOGIN_BTN).click()

    def enter_username(self, username_value):
        username_field = self.browser.find_element(*Locators.USERNAME_FIELD)
        username_field.click()
        username_field.send_keys(username_value)

    def enter_password(self, password_value):
        password_field = self.browser.find_element(*Locators.PASSWORD_FIELD)
        password_field.click()
        password_field.send_keys(password_value)

    def get_access_as_authorised_user(self):
        login_to_website = self.browser.find_element(*Locators.LOGIN_AS_AUTHORISED_USER)
        login_to_website.click()




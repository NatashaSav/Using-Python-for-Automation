from selenium import webdriver

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class Constants:
    URL: str = 'https://demo.seleniumeasy.com/basic-first-form-demo.html'


class Locators:
    USER_MSG = (By.XPATH, '//*[@id="user-message"]')
    SHOW_MSG = (By.XPATH, '//*[@id="get-input"]/button')
    FIRST_FIELD = (By.XPATH, '//*[@id="sum1"]')
    SECOND_FIELD = (By.XPATH, '//*[@id="sum2"]')
    TOTAL_BTN = (By.XPATH, '//*[@id="gettotal"]/button')


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_url(self, url: str):
        self.driver.get(url)

    def fill_text_field(self):
        message_field = self.driver.find_element(*Locators.USER_MSG)
        message_field.click()
        message_field.send_keys("Hello world")

    def show_message(self):
        show_message_button = self.driver.find_element(*Locators.SHOW_MSG)
        show_message_button.click()

    def fill_number_fields(self):
        first_field = self.driver.find_element(*Locators.FIRST_FIELD)
        first_field.send_keys('10')
        second_field = self.driver.find_element(*Locators.SECOND_FIELD)
        second_field.send_keys('12')

    def get_total_button(self):
        get_total_button = self.driver.find_element(*Locators.TOTAL_BTN)
        get_total_button.click()


if __name__ == "__main__":
    page = BasePage(driver=webdriver.Chrome())
    page.get_url(Constants.URL)
    page.fill_text_field()
    page.show_message()
    page.fill_number_fields()
    page.get_total_button()

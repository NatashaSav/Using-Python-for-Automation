from demo_seleniumeasy.pages.base_page import BasePage
from demo_seleniumeasy.pages.locators_page import Locators


class MainPage(BasePage):

    def __init__(self, browser, url):
        super().__init__(browser, url)

    def insert_single_input_field(self, text):
        self.send_keys_to_field(*Locators.USER_MSG, value=text)

    def insert_value_a(self, a_value):
        self.send_keys_to_field(*Locators.FIRST_FIELD, value=a_value)

    def insert_value_b(self, b_value):
        self.send_keys_to_field(*Locators.SECOND_FIELD, value=b_value)

    def check_show_message_button_name(self):
        return self.check_button_name(*Locators.SHOW_MSG_BTN)

    def check_get_total_button_name(self):
        return self.check_button_name(*Locators.GET_TOTAL_BTN)

    def click_show_message_button(self):
        self.click_on_button(*Locators.SHOW_MSG_BTN)

    def click_get_total_button(self):
        self.click_on_button(*Locators.GET_TOTAL_BTN)

    def get_total_number(self):
        return self.get_result_displayed_text(*Locators.DISPLAYED_TOTAL_VALUE)

    def get_text_from_message(self):
        return self.get_result_displayed_text(*Locators.DISPLAYED_TEXT)
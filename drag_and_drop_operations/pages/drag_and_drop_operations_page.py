from selenium.webdriver import ActionChains
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.wait import WebDriverWait

from drag_and_drop_operations.pages.base_page import BasePage
from drag_and_drop_operations.pages.locators_page import Locators
from selenium.webdriver.support import expected_conditions as EC


class DragAndDropOperationsPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)

    def get_list_of_capitals(self):
        return self.get_result_displayed_text(*Locators.LIST_OF_CAPITALS)

    def get_list_of_countries(self):
        return self.get_result_displayed_text(*Locators.LIST_OF_COUNTRIES)

    def wait_until_element_be_clickable(self, locator, timeout=10):
        wait = WebDriverWait(self.browser, timeout)
        return wait.until(EC.element_to_be_clickable(locator))

    def drag_action(self, locator):
        return self.wait_until_element_be_clickable(locator=locator, timeout=30)

    def drop_action(self, locator):
        return self.wait_until_element_be_clickable(locator=locator, timeout=30)

    def drag_and_drop_operations(self, locator: Locators):
        return ActionChains(self.browser).drag_and_drop(self.drag_action(locator=locator.DRAG_ACTION),
                                                        self.drop_action(locator=locator.DROP_ACTION)).perform()

    def get_background_color(self):
        return self.browser.find_element(*Locators.DRAG_ACTION).value_of_css_property('background-color')

    def get_rgb_color(self):
        return Color.from_string(self.get_background_color()).rgb

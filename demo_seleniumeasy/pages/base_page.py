class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def load_page(self):
        self.browser.get(self.url)

    def find_element_by_locator_name(self, *locator):
        return self.browser.find_element(*locator)

    def send_keys_to_field(self, *locator, value):
        self.find_element_by_locator_name(*locator).send_keys(value)

    def check_button_name(self, *locator):
        return self.find_element_by_locator_name(*locator).text

    def get_result_displayed_text(self, *locator):
        return self.find_element_by_locator_name(*locator).text

    def click_on_button(self, *locator):
        self.find_element_by_locator_name(*locator).click()
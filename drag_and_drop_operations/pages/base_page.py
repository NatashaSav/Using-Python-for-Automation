class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def load_page(self):
        self.browser.get(self.url)

    def get_title(self):
        return self.browser.title

    def find_element_by_locator_name(self, *locator):
        return self.browser.find_element(*locator)

    def get_result_displayed_text(self, *locator):
        return self.find_element_by_locator_name(*locator).text

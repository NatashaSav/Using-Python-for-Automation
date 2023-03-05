from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:

    def __init__(self, driver: WebDriver, url: str):
        self.driver = driver
        self.url = url

    def open_url(self):
        self.driver.get(self.url)

    def switch_to_main_page(self):
        parent = self.driver.window_handles[0]
        self.driver.switch_to.window(parent)

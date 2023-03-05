from selenium.webdriver.common.by import By


class Locators:
    HOME_BTN = (By.XPATH, '//a[@href="/"]')
    HOME_PAGE_TITLE = (By.CSS_SELECTOR, '.jumbotron.mt-4 .display-3')
    DONATION_SECTION = (By.CSS_SELECTOR, '.alert.alert-success')
    BLOG_BTN = (By.XPATH, '//a[@href="/blog/"]')
    ABOUT_URL = (By.XPATH, '//a[@href="/about/"]')
    CONTACT_URL = (By.XPATH, '//a[@href="/contact/"]')
    E_BOOK_URL = (By.XPATH, '//a[@href="https://leanpub.com/ultimateguidetoscrapy/"]')
    SUBSCRIBE_URL = (By.XPATH, '//a[@href="//eepurl.com/dmPGn9"]')
    SUBSCRIBE_TITLE = (By.CSS_SELECTOR, '.masthead')
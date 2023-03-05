import copy

from bs4 import BeautifulSoup
import requests
from selenium.webdriver.support.color import Color

from scraping_club.pages.base_page import BasePage
from scraping_club.pages.locators_page import Locators


class PageInfo(BasePage):

    def __init__(self, browser, url):
        super().__init__(browser, url)

    def get_response(self):
        response = requests.get(self.url)
        return response

    def get_response_content(self):
        return self.get_response().content

    def parse_html_to_lxml(self):
        response = self.get_response()
        return BeautifulSoup(response.text, 'lxml')

    def get_items_set(self):
        return self.get_items(self.parse_html_to_lxml())

    def pages_list(self):
        pagination = self.parse_html_to_lxml().find('ul', class_='pagination')
        return pagination.find_all('a', class_='page-link')

    def get_list_urls(self):
        urls = list()
        urls.append("?page=1")
        for page in self.pages_list():
            pageNum = int(page.text) if page.text.isdigit() else None
            if pageNum is not None:
                link = page.get('href')
                urls.append(link)
        return urls

    @staticmethod
    def get_items(soup: BeautifulSoup):
        return soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')

    @staticmethod
    def check_existence_of_price(item):
        return item.find('h5').text

    @staticmethod
    def check_existence_of_product_name(item):
        return item.find('h4', class_='card-title').text.strip('\n')

    @staticmethod
    def check_existence_of_product_image(item):
        return item.find('img').attrs['src']

    def get_list_price_titles_pictures(self, url):
        response = requests.get(url='https://scrapingclub.com/exercise/list_basic/' + url)
        items = self.get_items(soup=BeautifulSoup(response.text, 'lxml'))
        collected_items = []
        result = []
        for item in items:
            collected_items = copy.deepcopy(collected_items)
            product_name = self.check_existence_of_product_name(item)
            price = self.check_existence_of_price(item)
            picture = self.check_existence_of_product_image(item)
            result.append([product_name, price, picture])
        collected_items.append(result)
        return collected_items

    def get_general_info_about_items(self):
        results_for_all_pages = {}
        for url in self.get_list_urls():
            collected_items = self.get_list_price_titles_pictures(url)
            results_for_all_pages = copy.deepcopy(results_for_all_pages)
            results_for_all_pages[url] = collected_items
        return results_for_all_pages

    def open_home_page(self):
        return self.driver.find_element(*Locators.HOME_BTN).click()

    def get_home_page_title(self):
        return self.driver.find_element(*Locators.HOME_PAGE_TITLE).text

    def get_donation_section_title(self):
        return self.driver.find_element(*Locators.DONATION_SECTION).text

    def get_background_color(self):
        return self.driver.find_element(*Locators.DONATION_SECTION).value_of_css_property('background-color')

    def get_rgb_color(self):
        return Color.from_string(self.get_background_color()).rgb

    def open_blog_page(self):
        return self.driver.find_element(*Locators.BLOG_BTN).click()

    def get_picture(self):
        return self.driver.find_element()

    def open_about_page(self):
        return self.driver.find_element(*Locators.ABOUT_URL).click()

    def open_contact_page(self):
        return self.driver.find_element(*Locators.CONTACT_URL).click()

    def open_ebook_page(self):
        return self.driver.find_element(*Locators.E_BOOK_URL).click()

    def open_subscribe_page(self):
        return self.driver.find_element(*Locators.SUBSCRIBE_URL).click()

    def switch_to_first_page(self):
        return self.switch_to_main_page()

    def get_subscribe_title(self):
        return self.driver.find_element(*Locators.SUBSCRIBE_TITLE)








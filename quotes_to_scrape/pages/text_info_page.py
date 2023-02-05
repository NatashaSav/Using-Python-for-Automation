import requests
from bs4 import BeautifulSoup

from quotes_to_scrape.pages.base_page import BasePage


class TextInfo(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)

    def parse_text_to_lxml(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'lxml')
        return soup

    def get_quota_text(self):
        quoters = self.parse_text_to_lxml().find_all("span", class_="text")
        return quoters[00].text

    def get_author_name(self):
        authors = self.parse_text_to_lxml().find_all("small", class_="author")
        return authors[00].text

    def get_tags_name(self):
        tags = self.parse_text_to_lxml().find_all("div", class_="tags")
        return tags[00].text
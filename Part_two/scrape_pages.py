from bs4 import BeautifulSoup
import requests


class Constants:
    COUNT: int = 1
    URL: str = 'https://scrapingclub.com/exercise/list_basic/'


class PageInfo:

    @staticmethod
    def parse_html_to_lxml():
        response = requests.get(url=Constants.URL)
        soup = BeautifulSoup(response.text, 'lxml')
        return soup

    def get_items_from_lxml(self):
        items = self.get_items(self.parse_html_to_lxml())
        count = Constants.COUNT
        for item in items:
            self.print_price_item(item, count)
            count = count + Constants.COUNT

    def get_list_urls(self):
        pagination = self.parse_html_to_lxml().find('ul', class_='pagination')
        pages = pagination.find_all('a', class_='page-link')
        urls = []
        for page in pages:
            pageNum = int(page.text) if page.text.isdigit() else None
            if pageNum is not None:
                link = page.get('href')
                urls.append(link)
        return urls

    @staticmethod
    def get_items(soup: BeautifulSoup):
        return soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')

    @staticmethod
    def print_price_item(item, count: int):
        item_name = item.find('h4', class_='card-title').text.strip('\n')
        item_price = item.find('h5').text
        print('%s) Price: %s , Item Name: %s' % (count, item_price, item_name))

    def get_item_info(self):
        count = Constants.COUNT
        for url in self.get_list_urls():
            response = requests.get(url=Constants.URL + url)
            soup = BeautifulSoup(response.text, 'lxml')
            items = self.get_items(soup)
            for item in items:
                self.print_price_item(item, count)
                count = count + Constants.COUNT


if __name__ == "__main__":
    page_info = PageInfo()
    page_info.get_item_info()
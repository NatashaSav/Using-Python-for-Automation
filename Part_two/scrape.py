import requests
from bs4 import BeautifulSoup


class Constants:
    URL: str = 'http://quotes.toscrape.com/'


class TextInfo:

    @staticmethod
    def parse_text_to_lxml():
        response = requests.get(Constants.URL)
        soup = BeautifulSoup(response.text, 'lxml')
        return soup

    def get_info_by_text(self):
        quotes = self.parse_text_to_lxml().find_all("span", class_="text")
        authors = self.parse_text_to_lxml().find_all("small", class_="author")
        tags = self.parse_text_to_lxml().find_all("div", class_="tags")
        return [quotes, authors, tags]

    def print_text_info_in_console(self):
        for item in range(0, len(self.get_info_by_text()[0])):
            print(self.get_info_by_text()[0][item].text)
            print(self.get_info_by_text()[1][item].text)
            quote_tags = self.get_info_by_text()[2][item].find_all('a', class_='tag')
            for quoteTag in quote_tags:
                print(quoteTag.text)


if __name__ == "__main__":
    text_info = TextInfo()
    text_info.print_text_info_in_console()
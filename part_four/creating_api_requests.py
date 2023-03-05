import requests
import json


class Constants:
    URL: str = 'https://api.upcitemdb.com/prod/trial/lookup'
    PARAMETERS: dict = {'upc': '012993441012'}


class BasePage:
    @staticmethod
    def get_response():
        response = requests.get(Constants.URL, params=Constants.PARAMETERS)
        print(response.url)
        return response

    def get_content_items(self):
        content = self.get_response().content
        info = json.loads(content)
        item = info['items']
        item_info = item[0]
        title = item_info['title']
        brand = item_info['brand']
        print(title)
        print(brand)


if __name__ == "__main__":
    page = BasePage()
    page.get_content_items()

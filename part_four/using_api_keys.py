import requests


class Constants:
    URL: str = 'http://api.openweathermap.org'
    PARAMETERS: dict = {'APPID': '993dab9d4c7ef4ebf6742261d5a4e8c8', 'q': 'Seattle,US'}


class BasePage:
    @staticmethod
    def get_response():
        response = requests.get(Constants.URL, params=Constants.PARAMETERS)
        print(response.content)


if __name__ == "__main__":
    page = BasePage()
    page.get_response()

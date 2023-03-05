import requests


class ResponseInfo:
    def __init__(self, url: str):
        self.url = url

    def get_response(self):
        response = requests.get(self.url)
        return response
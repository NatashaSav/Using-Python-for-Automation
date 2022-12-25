import requests

baseUrl = 'http://api.openweathermap.org'
parameters = {'APPID': '993dab9d4c7ef4ebf6742261d5a4e8c8', 'q': 'Seattle,US'}
response = requests.get(baseUrl, params=parameters)
print(response.content)

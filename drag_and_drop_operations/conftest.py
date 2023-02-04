import json
import selenium.webdriver
import pytest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pathlib import Path

path_to_file = Path(__file__).parent.absolute().joinpath('config.json')


@pytest.fixture(scope='session')
def config():
    with open(path_to_file) as config_file:
        data = json.load(config_file)
    return data


@pytest.fixture(scope='session')
def browser():
    global driver
    driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
    return driver

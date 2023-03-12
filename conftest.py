import json
import os
import time

import selenium.webdriver
import pytest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def config(request):
    test_dir = os.path.dirname(request.module.__file__)
    with open(os.path.join(test_dir, "../../config.json")) as config_file:
        data = json.load(config_file)
    return data


@pytest.fixture(scope='session')
def browser():
    global driver
    driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    time.sleep(5)
    driver.quit()
    return driver

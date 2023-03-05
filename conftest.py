import json
import os
import time

import pathlib as pathlib
import selenium.webdriver
import pytest
from _pytest import pathlib
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pathlib import Path

# path_to_file = Path().joinpath('..\\..\\config.json').absolute()
# import pathlib
# path_to_file = pathlib.Path(__file__).parent.resolve().joinpath("..\\.config.json") - doesn't work
# path_to_file = Path.cwd().joinpath("..\\..\\config.json")
# project_root = os.path.dirname(os.path.dirname(__file__))
# path_to_file = "PythonAQa\\..\\..\\config.json"
# result = f'{project_root}{path_to_file}'

# current_project = os.path.dirname(__file__)
# smt = Path(current_project)
# target_path_1 = Path(current_project).joinpath("..\\config.json")
# target_path_1 = os.path.join(current_project, '\\..\\config.json')
# folder_name = Path(__file__).cwd().parent.parent
# target_path_1 = f'{folder_name}\\{"config.json"}'
# target_path_1 = folder_name.joinpath("config.json")
# path_to_file = os.path.abspath('..\\..\\config.json')

#option 1 - WORK!!!!
# project_root = os.path.dirname(os.path.dirname(__file__))
# path_to_config_file = '\\PythonAQa\\quotes_to_scrape\\config.json'
# path_to_file = f'{project_root}{path_to_config_file}'

#option 2 - DOESN'T WORK
# project_root = os.path.dirname(os.path.dirname(__file__))
# path_to_config_file = '\\PythonAQa\\..\\config.json'
# path_to_file = f'{project_root}{path_to_config_file}'

#option 3
# project_root = Path(os.getcwd())
# path_to_config_file = '\\config.json'
# path_to_file = f'{project_root}{path_to_config_file}'
# print(path_to_file)
# 'C:\\Users\\Nataliia_Osnovenko\\PythonCreatingNewBddScenarios\\PythonAQa\\scraping_club\\config.json'

#option 4
project_root = os.path.dirname(__file__)
folder_name = pathlib.Path().absolute().parent.parent.name
path_to_config_file = f'{folder_name}\\{"config.json"}'
path_to_file = f'{project_root}\\{path_to_config_file}'

# project_root = Path(os.getcwd())
# folder_name = pathlib.Path().absolute().parent.parent.name
# path_to_config_file = '\\config.json'
# res = folder_name.join(path_to_config_file)
# path_to_file = f"{project_root}{folder_name}{path_to_config_file}"


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
    time.sleep(5)
    driver.quit()
    return driver

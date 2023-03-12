from pytest_bdd import scenarios, when, then, given, parsers

from drag_and_drop_operations.pages.drag_and_drop_operations_page import DragAndDropOperationsPage
from drag_and_drop_operations.pages.locators_page import Locators
from drag_and_drop_operations.pages.requests_page import ResponseInfo

scenarios('../features')


@given(parsers.parse('I have an url'), target_fixture='main_function')
def main_function(browser, config):
    return DragAndDropOperationsPage(browser=browser, url=config['URLS']['MAIN_URL'])


@given(parsers.parse('I open the main page'))
def open_page(main_function, config):
    main_function.load_page()
    current_url = main_function.browser.current_url
    assert config['URLS']['MAIN_URL'] == current_url, \
        f"expected url {config['URLS']['MAIN_URL']} and {current_url} current url don't match"


@when(parsers.parse('I check that status code of the page is "{status_code}"'), converters={"status_code": int})
def get_status_code(status_code, config):
    response_page = ResponseInfo(url=config['URLS']['MAIN_URL'])
    response_status_code = response_page.get_response().status_code
    assert response_status_code == status_code, f"expected to get {status_code}, but received another" \
                                                f" {response_status_code} code"


@then(parsers.parse('I have to check that current page has title "{title}"'), converters={"title": str})
def get_title(main_function, title):
    actual_title = main_function.get_title()
    assert actual_title == title, f"expected to get {title}, but {actual_title} received"


@when(parsers.parse('I check that "{capital_name}" is in list of capitals'), converters={"capital_name": str})
def verify_existence_of_capital_in_the_list(main_function, capital_name):
    list_of_capitals = main_function.get_list_of_capitals()
    assert capital_name in list_of_capitals, f"capital name {capital_name} doesn't exist in list of " \
                                             f"capitals {list_of_capitals}"


@when(parsers.parse('"{country_name}" is in list of countries'), converters={"country_name": str})
def verify_existence_of_country_in_the_list(main_function, country_name):
    list_of_countries = main_function.get_list_of_countries()
    assert country_name in list_of_countries, f"country name {country_name} doesn't exist in " \
                                              f"list of countries {list_of_countries}"


@then(parsers.parse('I drag capital name and move it to country name'))
def drag_and_drop(main_function):
    main_function.drag_and_drop_operations(locator=Locators())


@then(parsers.parse('I verify that capital background is "{rgb_color}"'), converters={"rgb_color": str})
def check_color_of_capital_block(main_function, rgb_color):
    background_color = main_function.get_rgb_color()
    assert background_color == rgb_color, f"expected to see {rgb_color}, but {background_color} color received"

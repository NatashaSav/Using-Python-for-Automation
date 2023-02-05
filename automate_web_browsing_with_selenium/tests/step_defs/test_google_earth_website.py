from pytest_bdd import scenarios, given, when, then, parsers

from automate_web_browsing_with_selenium.pages.operations_with_shadow_root import OperationsWithShadowRoot
from automate_web_browsing_with_selenium.pages.requests_page import ResponseInfo

scenarios('../features')


@given(parsers.parse('I have an url'), target_fixture='main_function')
def main_function(browser, config):
    return OperationsWithShadowRoot(browser=browser, url=config['URLS']['MAIN_URL'])


@given('I open the main page')
def open_page(main_function):
    main_function.open_url()


@when(parsers.parse('I check that status code of the page is "{status_code}"'), converters={"status_code": int})
def get_status_code(status_code, config):
    response_page = ResponseInfo(url=config['URLS']['MAIN_URL'])
    response = response_page.get_response()
    assert response.status_code == status_code, "received another status code"


@then(parsers.parse('I have to check that current page has title "{title}"'), converters={"title": str})
def get_title(main_function, title):
    actual_title = main_function.driver.title
    assert actual_title == title, "received another title"


@then(parsers.parse('I check that icon "{icon}" is one the page'), converters={"icon": str})
def check_existence_icon_on_the_page(main_function, icon):
    actual_icon = main_function.driver.page_source
    assert icon in actual_icon, "icon was changed"


@then(parsers.parse('I click on Menu button'))
def verify_menu_button(main_function):
    main_function.click_menu_btn()




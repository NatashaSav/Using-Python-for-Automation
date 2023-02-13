from pytest_bdd import scenarios, given, when, then, parsers

from automate_web_browsing_with_selenium.pages.operations_with_shadow_root import OperationsWithShadowRoot
from automate_web_browsing_with_selenium.pages.requests_page import ResponseInfo

scenarios('../features')


@given(parsers.parse('I have an url'), target_fixture='main_function')
def main_function(browser, config):
    return OperationsWithShadowRoot(browser=browser, url=config['URLS']['MAIN_URL'])


@given(parsers.parse('I open "{url}" page'), converters={"utl": str})
def open_page(main_function, url):
    main_function.open_url()
    current_url = main_function.driver.current_url
    assert url in current_url, f"current_url {current_url} and expected url {url} don't match"


@when(parsers.parse('I check that status code of the page is "{status_code}"'), converters={"status_code": int})
def get_status_code(status_code, config):
    response_page = ResponseInfo(url=config['URLS']['MAIN_URL'])
    response_status_code = response_page.get_response().status_code
    assert response_status_code == status_code, f"expected {status_code} status code," \
                                                f" but received {response_status_code}"


@then(parsers.parse('I have to check that current page has title "{title}"'), converters={"title": str})
def get_title(main_function, title):
    actual_title = main_function.driver.title
    assert actual_title == title, f"expected title {title}, but received {actual_title}"


@then(parsers.parse('I check that icon "{icon}" is one the page'), converters={"icon": str})
def check_existence_icon_on_the_page(main_function, icon):
    actual_icon = main_function.driver.page_source
    assert icon in actual_icon, f"expected to get icon {icon}, but another icon appeared"


@when(parsers.parse('I click on Menu button'))
def verify_menu_button(main_function):
    main_function.click_menu_btn()
    return main_function


@then(parsers.parse('I see "{sign_in}" appeared on the page'), converters={"sign_in": str})
def get_logo_img(main_function, sign_in):
    sign_in_text = main_function.get_sign_in_value()
    assert sign_in in sign_in_text, f"expected to see {sign_in} text on the page"

from pytest_bdd import scenarios, given, when, then, parsers

from automate_web_browsing_with_selenium.pages.requests_page import ResponseInfo
from quotes_to_scrape.pages.login_page import Login, Credentials
from quotes_to_scrape.pages.text_info_page import TextInfo

scenarios('../features')


@then(parsers.parse("I have Login button"), target_fixture='login_function')
def login_function(browser):
    return Login(browser=browser)


@given(parsers.parse('I have an url'), target_fixture='main_function')
def main_function(browser, config):
    return TextInfo(browser=browser, url=config['URLS']['MAIN_URL'])


@given(parsers.parse('I open the main page'))
def open_page(main_function, config):
    main_function.open_url()
    current_url = main_function.driver.current_url
    assert config['URLS']['MAIN_URL'] == current_url, \
        f"expected url {config['URLS']['MAIN_URL']} and {current_url}  current url don't match"


@when(parsers.parse('I check that status code of the page is "{status_code}"'), converters={"status_code": int})
def get_status_code(status_code, config):
    response_page = ResponseInfo(url=config['URLS']['MAIN_URL'])
    response_status_code = response_page.get_response().status_code
    assert response_status_code == status_code, f"expected {status_code},but " \
                                                f"received {response_status_code} status code"


@then(parsers.parse('I check that current page has title "{title}"'), converters={"title": str})
def get_title(main_function, title):
    actual_title = main_function.driver.title
    assert actual_title == title, f"expected {title}, but received another title {actual_title}"


@when(parsers.parse('I click on Login button to get to the site'))
def click_login_btn(login_function):
    login_function.click_login()


@then(parsers.parse('I enter username "{username}"'), converters={"username": str})
def fill_username_field(login_function, username):
    login_function.enter_username(username)
    assert Credentials.USERNAME == username, f"expected {username} username, but received {Credentials.USERNAME}"


@then(parsers.parse('I enter password "{password}"'), converters={"password": str})
def fill_password_field(login_function, password):
    login_function.enter_password(password)
    assert Credentials.PASSWORD == password, f"expected {password} password, but received {Credentials.PASSWORD}"


@then(parsers.parse('I click on Login button and get to the site as authorised user'))
def login_to_website(login_function):
    login_function.get_access_as_authorised_user()


@when(parsers.parse('I see that first quote has text "{quote_text}"'), converters={"quote_text": str})
def get_quote_text(main_function, quote_text):
    actual_quote_text = main_function.get_quota_text()
    assert actual_quote_text == quote_text, f"{quote_text} and {actual_quote_text} texts don't match"


@then(parsers.parse('I expect to see "{author_name}" author name'), converters={"author_name": str})
def get_author_name(main_function, author_name):
    actual_author_name = main_function.get_author_name()
    assert actual_author_name == author_name, f"{author_name} and {actual_author_name} author names don't match"


@then(parsers.parse('I want to be sure that "{tag_1}", "{tag_2}", "{tag_3}" and "{tag_4}" tags are in the first quote'),
      converters={"tag_1": str, "tag_2": str, "tag_3": str, "tag_4": str})
def get_tags_name(main_function, tag_1, tag_2, tag_3, tag_4):
    actual_tags_name = main_function.get_tags_name()
    assert tag_1 in actual_tags_name, f"tag_1 {tag_1} is not in the list of tags {actual_tags_name}"
    assert tag_2 in actual_tags_name, f"tag_2 {tag_2} is not in the list of tags {actual_tags_name}"
    assert tag_3 in actual_tags_name, f"tag_3 {tag_3} is not in the list of tags {actual_tags_name}"
    assert tag_4 in actual_tags_name, f"tag_4 {tag_4} is not in the list of tags {actual_tags_name}"


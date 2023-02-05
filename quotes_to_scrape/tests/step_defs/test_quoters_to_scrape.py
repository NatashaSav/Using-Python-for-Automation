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


@given('I open the main page')
def open_page(main_function):
    main_function.open_url()


@then(parsers.parse('I check that the main page has "{url}" url'), converters={"url": str})
def check_url(main_function, url):
    current_url = main_function.url
    assert current_url == url, "url was changed"


@when(parsers.parse('I check that status code of the page is "{status_code}"'), converters={"status_code": int})
def get_status_code(status_code, config):
    response_page = ResponseInfo(url=config['URLS']['MAIN_URL'])
    response = response_page.get_response()
    assert response.status_code == status_code, "received another status code"


@then(parsers.parse('I check that current page has title "{title}"'), converters={"title": str})
def get_title(main_function, title):
    actual_title = main_function.driver.title
    assert actual_title == title, "received another title"


@when(parsers.parse('I click on Login button to get to the site'))
def click_login_btn(login_function):
    login_function.click_login()


@then(parsers.parse('I enter username "{username}"'), converters={"username": str})
def fill_username_field(login_function, username):
    login_function.enter_username(username)
    assert Credentials.USERNAME == username, "wrong username"


@then(parsers.parse('I enter password "{password}"'), converters={"password": str})
def fill_password_field(login_function, password):
    login_function.enter_password(password)
    assert Credentials.PASSWORD == password, "wrong password"


@then(parsers.parse('I click on Login button and get to the site as authorised user'))
def login_to_website(login_function):
    login_function.get_access_as_authorised_user()


@when(parsers.parse('I see that first quote has text "{quote_text}"'), converters={"quote_text": str})
def get_quote_text(main_function, quote_text):
    actual_quote_text = main_function.get_quota_text()
    assert actual_quote_text == quote_text, "texts don't match"


@then(parsers.parse('I expect to see "{author_name}" author name'), converters={"author_name": str})
def get_author_name(main_function, author_name):
    actual_author_name = main_function.get_author_name()
    assert actual_author_name == author_name, "author names don't match"


@then(parsers.parse('I want to be sure that "{tag_1}", "{tag_2}", "{tag_3}" and "{tag_4}" tags are in the first quote'),
      converters={"tag_1": str, "tag_2": str, "tag_3": str, "tag_4": str})
def get_tags_name(main_function, tag_1, tag_2, tag_3, tag_4):
    actual_tags_name = main_function.get_tags_name()
    assert tag_1 in actual_tags_name, "tag_1 don't match"
    assert tag_2 in actual_tags_name, "tag_2 don't match"
    assert tag_3 in actual_tags_name, "tag_3 don't match"
    assert tag_4 in actual_tags_name, "tag_4 don't match"


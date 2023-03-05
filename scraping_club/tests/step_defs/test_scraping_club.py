from pytest_bdd import scenarios, given, when, then, parsers

from automate_web_browsing_with_selenium.pages.requests_page import ResponseInfo
from scraping_club.pages.scrape_price_and_item_name_page import PageInfo

scenarios('../features')


@given(parsers.parse('I have an url'), target_fixture='main_function')
def main_function(browser, config):
    return PageInfo(browser=browser, url=config['URLS']['MAIN_URL'])


@given(parsers.parse('I open the main page'))
def open_page(main_function, config):
    main_function.open_url()
    current_url = main_function.driver.current_url
    assert config['URLS']['MAIN_URL'] == current_url, \
        f"expected url {config['URLS']['MAIN_URL']} and {current_url} current url don't match"


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


@then(parsers.parse('I check that all product names, prices and pictures are available on the pages'))
def get_item_data(main_function):
    general_info = main_function.get_general_info_about_items()
    for page_number, collected_page_info in general_info.items():
        for selected_page in collected_page_info:
            for card in selected_page:
                assert card[0] is not None, "card title is disappeared"
                assert card[1] is not None, "product price is disappeared"
                assert card[2] is not None, "product picture is disappeared"


@when(parsers.parse('I click on Home button'))
def get_home_button(main_function, config):
    main_function.open_url()
    main_function.open_home_page()
    current_url = main_function.driver.current_url
    assert config['URLS']['URL'] == current_url, \
        f"expected url {config['URLS']['MAIN_URL']} and {current_url} current url don't match"


@then(parsers.parse('I check that "{text}" is appeared on current page'), converters={"text": str})
def get_main_text_on_home_page(main_function, text):
    home_page_title = main_function.get_home_page_title()
    assert home_page_title == text, f"expected {text}, but received another title {home_page_title}"


@then(parsers.parse('I see container with name "{title}"'), converters={"title": str})
def get_donation_container(main_function, title):
    donation_title = main_function.get_donation_section_title()
    assert title in donation_title, f"expected {title}, but received another title {donation_title}"


@then(parsers.parse('I need to make sure that container has {rgb_color} color'), converters={"rgb_color": str})
def verify_container_color(main_function, rgb_color):
    background_color = main_function.get_rgb_color()
    return background_color == rgb_color, f"expected to see {rgb_color}, but {background_color} color received"


@when(parsers.parse('I click on Blog button'))
def get_home_button(main_function, config):
    main_function.open_url()
    main_function.open_blog_page()
    current_url = main_function.driver.current_url
    assert config['URLS']['BLOG_URL'] == current_url, \
        f"expected url {config['URLS']['BLOG_URL']} and {current_url} current url don't match"


@then(parsers.parse('I check that "{picture}" picture is on the page'), converters={"picture": str})
def get_picture_scr(main_function, picture):
    picture_src = main_function.driver.page_source
    assert picture in picture_src, f"expected {picture}, but received another url"


@when(parsers.parse('I click on About button'))
def get_home_button(main_function, config):
    main_function.open_url()
    main_function.open_about_page()
    current_url = main_function.driver.current_url
    assert config['URLS']['ABOUT_URL'] == current_url, \
        f"expected url {config['URLS']['BLOG_URL']} and {current_url} current url don't match"


@when(parsers.parse('I click on Contact button'))
def get_home_button(main_function, config):
    main_function.open_url()
    main_function.open_contact_page()
    current_url = main_function.driver.current_url
    assert config['URLS']['CONTACT_URL'] == current_url, \
        f"expected url {config['URLS']['CONTACT_URL']} and {current_url} current url don't match"


@when(parsers.parse('I click on eBook button'))
def get_home_button(main_function, config):
    main_function.open_url()
    main_function.open_ebook_page()
    current_url = main_function.driver.page_source
    assert config['URLS']['E_BOOK_URL'] in current_url, \
        f"expected url {config['URLS']['E_BOOK_URL']} and {current_url} current url don't match"


@when(parsers.parse('I click on Subscribe button'))
def get_home_button(main_function):
    main_function.switch_to_first_page()
    main_function.open_subscribe_page()


@then(parsers.parse('I check that current page has "{title}" title'), converters={"title": str})
def get_subscribe_title(main_function, title):
    actual_title = main_function.get_subscribe_title().text
    assert actual_title == title, f"expected {actual_title}, but received another title {title}"


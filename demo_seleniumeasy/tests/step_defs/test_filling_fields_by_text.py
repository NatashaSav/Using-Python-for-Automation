from pytest_bdd import scenarios, when, then, given, parsers
from demo_seleniumeasy.pages import MainPage

scenarios('../features')


@given(parsers.parse('I have an url'), target_fixture='base_function')
def base_function(browser, config):
    return MainPage(browser=browser, url=config['URLS']['MAIN_URL'])


@given(parsers.parse('I open the main page'))
def open_page(base_function, config):
    base_function.load_page()
    current_url = base_function.browser.current_url
    assert config['URLS']['MAIN_URL'] == current_url, \
        f"expected url {config['URLS']['MAIN_URL']} and {current_url} current url don't match"


@when(parsers.parse('the user type "{text}"'), converters={"text": str})
def input_text_in_single_field(base_function, text):
    base_function.insert_single_input_field(text)


@when(parsers.parse('the user type "{number}" in field named a'), converters={"number": int})
def input_number_in_field_a(base_function, number):
    base_function.insert_value_a(number)


@when(parsers.parse('the user type "{number}" in field named b'), converters={"number": int})
def input_number_in_field_b(base_function, number):
    base_function.insert_value_b(number)


@then(parsers.parse('"{number}" number is displayed on the page'), converters={"number": str})
def get_total_number(base_function, number):
    total_number = base_function.get_total_number()
    assert number == total_number, f"expected to get {number}, but {total_number} number displayed on the page"


@then('the user click Show Message button')
def click_login(base_function):
    base_function.click_show_message_button()


@then(parsers.parse('the user find the "{button_name}" button in the two input fields'),
      converters={"button_name": str})
def check_button_name(base_function, button_name):
    actual_button_name = base_function.check_get_total_button_name()
    assert (button_name == actual_button_name), f"{actual_button_name} and " \
                                                f"{button_name} button name do not match"


@then(parsers.parse('the user find the "{button_name}" button in the single input field'),
      converters={"button_name": str})
def check_button_name_(base_function, button_name):
    actual_button_name = base_function.check_show_message_button_name()
    assert (button_name == actual_button_name), f"actual {actual_button_name} and " \
                                                f"expected {button_name} button name don't match"


@then('the user click on Get Total button')
def click_get_total_button(base_function):
    base_function.click_get_total_button()


@then(parsers.parse('"{message}" message is displayed on page'), converters={"message": str})
def check_appeared_message(base_function, message):
    actual_message = base_function.get_text_from_message()
    assert (message == actual_message), f" expected {message}, but {actual_message} displayed on the page"
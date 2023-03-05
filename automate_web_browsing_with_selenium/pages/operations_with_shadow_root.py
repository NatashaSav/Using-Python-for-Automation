from automate_web_browsing_with_selenium.pages.base_page import BasePage
from automate_web_browsing_with_selenium.pages.locators_page import Locators


class ShadowRootInfo:
    SHADOW_ROOT: str = 'return arguments[0].shadowRoot'


class OperationsWithShadowRoot(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)

    def click_menu_btn(self):
        earth_app = self.driver.find_element(*Locators.EARTH_APP)
        shadow_earth_app = self.driver.execute_script(ShadowRootInfo.SHADOW_ROOT, earth_app)

        toolbar = shadow_earth_app.find_element(*Locators.TOOLBAR)
        toolbar_shadow = self.driver.execute_script(ShadowRootInfo.SHADOW_ROOT, toolbar)

        menu_btn = toolbar_shadow.find_element(*Locators.MENU_BTN)
        launch_menu_btn = self.wait_until_element_be_clickable(locator=menu_btn, timeout=60)
        self.sleep_during_specific_time()
        launch_menu_btn.click()

    def get_sign_in_value(self):
        earth_app = self.driver.find_element(*Locators.EARTH_APP)
        return earth_app.text
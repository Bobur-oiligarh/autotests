from appium.webdriver.webdriver import WebDriver

from mobile_testing.pages.base_page import Page
from appium.webdriver.common.appiumby import AppiumBy as AppBy
from appium_flutter_finder.flutter_finder import FlutterFinder, FlutterElement


def print_elements(elements):
    for element in elements:
        print()
        print(element)
        print(element.tag_name)
        # print(element.accessible_name)
        print(element.id)
        print(element.location)
        print(element.rect)
        print(element.parent)
        print()


class SMSKeyPage(Page):
    PAGE_VIEW = (AppBy.CLASS_NAME, "android.view.View")
    SMS_KEY_FIELD = (AppBy.CLASS_NAME, "android.view.View")

    def get_page_text(self):
        return self.find_element(*self.PAGE_VIEW).text

    def get_sms_key_field(self):
        return self.find_element_xpath(*self.SMS_KEY_FIELD)

    def send_sms_key(self, key):
        element = self.get_sms_key_field()
        element.click()
        element.send_keys(key)

from mobile_testing.pages.registration.set_phone_page import SetPhonePage, LangSelector
from mobile_testing.pages.registration.sms_key_page import SMSKeyPage


class Application:

    def __init__(self, driver):
        self.set_phone_number = SetPhonePage(driver)
        self.sms_key_page = SMSKeyPage(driver)

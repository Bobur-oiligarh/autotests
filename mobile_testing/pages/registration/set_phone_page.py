from appium.webdriver.common.appiumby import AppiumBy as AppBy

from mobile_testing.pages.base_page import Page


class SetPhonePage(Page):
    PHONE_FIELD = (AppBy.CLASS_NAME, "android.widget.EditText")
    LANG_SELECTOR = (AppBy.CLASS_NAME, "android.widget.ImageView")
    PROCEED_BUTTON = (AppBy.CLASS_NAME, "android.widget.Button")

    def click_phone_field(self):
        self.click(*self.PHONE_FIELD)

    def set_phone_field_value(self, number: str):
        self.input(number, *self.PHONE_FIELD)

    def click_lang_selector(self):
        self.click(*self.LANG_SELECTOR)

    def click_proceed(self):
        self.click(*self.PROCEED_BUTTON)


class LangSelector(Page):
    RU = (AppBy.NAME, "Russian")
    UZ = (AppBy.NAME, "O'zbek lotin")
    EMPTINESS = (AppBy.CLASS_NAME, "android.view.View")

    def select_ru(self):
        self.click(*self.RU)

    def select_uz(self):
        self.click(*self.UZ)

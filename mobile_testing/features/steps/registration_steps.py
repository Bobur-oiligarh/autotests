from behave import *


@given("input phone number")
def input_phone(context):
    context.app.set_phone_number.set_phone_field_value("941775859")


@when("press button proceed")
def press_proceed(context):
    context.app.set_phone_number.click_proceed()


@then("The SMS key window opens")
def check_opened_sms_key_window(context):
    context.app.sms_key_page.send_sms_key(12345)

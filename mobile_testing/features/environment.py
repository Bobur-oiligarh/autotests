from appium.webdriver import Remote
from appium.webdriver.common.appiumby import AppiumBy

from mobile_testing.app.application import Application


def before_scenario(context, scenario):
    desired_caps = {
        "deviceName": "Nexus 7",
        "platformName": "Android",
        "version": "7.1",
        "app": "C:\\Users\\ivanc\\Desktop\\app-release (4).apk"
    }
    context.driver = Remote("http://localhost:4723/wd/hub", desired_caps)
    context.driver.implicitly_wait(100)
    context.app = Application(context.driver)


# def after_scenario(context, scenario):
    # context.driver.quit()

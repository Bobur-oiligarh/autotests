from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy


class Page:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def click(self, *locator):
        self.find_element(*locator).click()

    def input(self, text, *locator):
        self.click(*locator)
        e = self.find_element(*locator)
        e.clear()
        e.set_text(text)

    def find_element_xpath(self, *lokator):
        elements = self.driver.find_elements(*lokator)

        for i in range(len(elements)):
            print()
            print(elements[i].__dict__)
            print(str(i))
            print()
            elements[i].click()
            elements[i].send_keys(str(i))
        return elements[4]

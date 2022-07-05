from selenium import webdriver
from appium import webdriver as app_driver

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/")

print(driver.title)

driver.quit()

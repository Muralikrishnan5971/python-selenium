from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import time

s = Service("/driver/chromdriver")
driver = webdriver.Chrome(service = s)
driver.get("https://www.saucedemo.com/")
print(driver.title)
print(driver.current_url)

driver.quit()

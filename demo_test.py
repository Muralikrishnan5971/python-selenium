from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time

s = Service("/driver/chromdriver")
driver = webdriver.Chrome(service = s)

# s = Service("/driver/geckodriver")
# driver = webdriver.Firefox(service = s)       need to have firefox locally installed

driver.maximize_window()
driver.get("https://www.saucedemo.com/")
print(driver.title)
print(driver.current_url)

# id, xpath, css selector, classname, name, linktext
driver.find_element(By.NAME, "user-name").send_keys("standard_user")
driver.find_element(By.NAME, "password").send_keys("secret_sauce")

driver.find_element(By.ID, "login-button").submit()
time.sleep(3)

print(driver.title)
element_text = driver.find_element(By.XPATH, "(//div[@class='inventory_item_name'])[1]").text
print(element_text)

assert "Labs Backpack" in element_text

driver.quit()

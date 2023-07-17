from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

s = Service("/driver/chromdriver")
driver = webdriver.Chrome(service = s)
driver.maximize_window()
driver.get("https://www.globalsqa.com/demo-site/select-dropdown-menu/")
print(driver.title)

driver.find_element(By.ID, )

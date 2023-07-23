import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

pytestmark = [pytest.mark.regression, pytest.mark.murali]
# pytestmark = pytest.mark.regression

@pytest.mark.integration
@pytest.mark.smoke
def test_lamda_ecommerce_search():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://ecommerce-playground.lambdatest.io/")
    driver.find_element(By.NAME, "search").send_keys("smasung")
    driver.find_element(By.XPATH, "(//button[@type = 'submit'])[1]").click()
    search_item = driver.title
    
    assert search_item.__contains__("smasung")

@pytest.mark.skip
def test_end_to_end():
    print("End to End Tests")

@pytest.mark.login
@pytest.mark.smoke
def test_login():
    print("Log into Application")

@pytest.mark.logout
@pytest.mark.smoke
def test_logout():
    print("Log out of the application")

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

driver = webdriver.Chrome()

@pytest.fixture(autouse=True)
def start_automatic_fixture():
    print("Test started with automatic fixture")

@pytest.fixture(scope="module")
def setup_teardown():
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=common/home")
    driver.find_element(By.XPATH, "(//a[@role = 'button' and @data-toggle = 'dropdown'])[3]").click()
    time.sleep(3)
    driver.find_element(By.ID, "input-email").send_keys("muralikrishnan.pro@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys("pytest@123")
    driver.find_element(By.XPATH, "//input[@value = 'Login']").click()
    title = driver.title
    assert title == "My Account"
    print("-- Logged In --")

    yield
    click_on_right_column("Logout")
    title = driver.title
    assert title == "Account Logout"
    print("-- Logged Out --")

@pytest.mark.usefixtures("setup_teardown")
def test_notification():
    
    click_on_right_column("Notification")
    title = driver.title
    assert title == "Subscribed products"
    driver.find_element(By.XPATH, "//a[contains(text(), 'Continue')]").click()
    print("-- Test 1 Complete --")


@pytest.mark.usefixtures("setup_teardown")
def test_order_history():
     
    click_on_right_column("Order History")
    title = driver.title
    assert title == "Order History"
    print("-- Test 2 Complete --")

def click_on_right_column(text):
    right_column_list = driver.find_elements(By.XPATH, "//aside[@id = 'column-right']/div/a")
    for item in right_column_list:
        if item.text == text:
            item.click()
            break
    time.sleep(3)

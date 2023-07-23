import softest
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class AssertionTests(softest.TestCase):
    pass

    @pytest.mark.filterwarnings
    def test_ecommerce_search_apple_tablet(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(15)
        driver.get("https://ecommerce-playground.lambdatest.io/")
        driver.find_element(By.XPATH, "(//button[@type = 'button'])[1]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "(//a[@data-category_id= '57'])[1]").click()
        time.sleep(2)
        driver.find_element(By.NAME, "search").send_keys("apple")
        driver.find_element(By.XPATH, "(//button[@type = 'submit'])[1]").click()
        time.sleep(4)
        search_item = driver.find_element(By.XPATH, "//div[contains(@id, 'entry')]/h1").text
        print(search_item)       
        print("Search Item object id: \t", id(search_item))
        print("Search Item object id: \t", id("Search - apple"))

        self.soft_assert(self.assertIs(
            "Search - apple", search_item,
            "Expected and Actual texts don't match"))
        
        self.soft_assert(self.assertTrue(
            driver.title.__contains__("Search - apple")))

        self.soft_assert(self.assertIn(
            "apple" in search_item, "Apple search keyword is not present"))
        
        self.assert_all()
        

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

class Test_Raw:
    textbox_username_xpath = "//input[@id='UserName']"
    def test_01 (self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        self.driver.get("https://us.erp.gold/")
        self.driver.maximize_window()
        self.driver.find_element(By.XPATH, self.textbox_username_xpath)
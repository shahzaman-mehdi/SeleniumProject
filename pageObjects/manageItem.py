from selenium import webdriver
from selenium.webdriver.common.by import By
class ItemManagement:

    list_advanceInventory_linktxt = "Advance Inventory"
    link_itemMasterNav_xpath = '//*[@id="panel_3124"]/li[2]/a'
    button_addItem_xpath = '//*[@id="headingRow"]/tbody/tr/td[1]/a'
    list_itemCategory_dropdown = '//*[@id="icform"]/div[2]/div[1]/span[2]/span/span[2]'
    link_itemCategoryValue_linktxt = "PHONE"

    def __init__(self, driver):
        self.driver = driver

    def clickInventoryNav(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, self.list_advanceInventory_linktxt).click()

    def clickItemMasterNav(self):
        self.driver.find_element(By.XPATH, self.link_itemMasterNav_xpath).click()

    def clickAddItem(self):
        self.driver.find_element(By.XPATH, self.button_addItem_xpath).click()

    def clickCategoryLink(self):
        self.driver.find_element(By.XPATH, self.list_itemCategory_dropdown).click()

    def selectItemCategoryValue(self):
        self.driver.find_element(By.XPATH, self.link_itemCategoryValue_linktxt).click()




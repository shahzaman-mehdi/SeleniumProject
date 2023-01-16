from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class ItemManagement:
    list_advanceInventory_linktxt = "Advance Inventory"
    link_itemMasterNav_linktxt = 'Item Master'
    button_addItem_xpath = '//*[@id="headingRow"]/tbody/tr/td[1]/a'
    textbox_itemCode_xpath = "//input[@id='ItemCode']"
    textbox_itemName_id = "ItemName"
    textbox_itemDescription_xpath = "//input[@id='ItemDescription']"
    textbox_upcNumber_xpath = "//input[@id='UPCCode']"
    textbox_standardCost_xpath = "//input[@id='Item_Weight_LB']"
    textbox_sellingPrice_id = "UnitPrice"
    button_saveItem_id = 'btnContinueSave'

    def __init__(self, driver):
        self.driver = driver

    def clickInventoryNav(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, self.list_advanceInventory_linktxt).click()

    def clickItemMasterNav(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, self.link_itemMasterNav_linktxt).click()

    def clickAddItem(self):
        self.driver.find_element(By.XPATH, self.button_addItem_xpath).click()

    def enterItemCode(self, code):
        self.driver.find_element(By.XPATH, self.textbox_itemCode_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_itemCode_xpath).send_keys(code)

    def enterItemName(self, name):
        self.driver.find_element(By.ID, self.textbox_itemName_id).send_keys(name)

    def enterItemDescription(self, description):
        self.driver.find_element(By.XPATH, self.textbox_itemDescription_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_itemDescription_xpath).send_keys(description)

    def enterUPCNumber(self, upc):
        self.driver.find_element(By.XPATH, self.textbox_upcNumber_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_upcNumber_xpath).send_keys(upc)

    def enterStandardCost(self, stdCost):
        self.driver.find_element(By.XPATH, self.textbox_standardCost_xpath).click()
        self.driver.find_element(By.XPATH, self.textbox_standardCost_xpath).send_keys(stdCost)

    def enterSellingPrice(self, sellPrice):
        self.driver.find_element(By.ID, self.textbox_sellingPrice_id).click()
        self.driver.find_element(By.ID, self.textbox_sellingPrice_id).send_keys(sellPrice)

    def clickSaveAndContinue(self):
        self.driver.find_element(By.ID, self.button_saveItem_id).click()

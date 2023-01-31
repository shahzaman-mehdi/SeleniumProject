import time
from selenium.webdriver.common.by import By


class ItemManagement:
    list_advanceInventory_linktxt = "Advance Inventory"
    link_itemMasterNav_linktxt = 'Item Master'
    button_addItem_xpath = '//*[@id="headingRow"]/tbody/tr/td[1]/a'
    dropdown_itemCategory_xpath = "//*[@id='icform']/div[2]/div[1]/span[2]"
    select_itemCategory_xpath = "//*[@id='ItemCategoryID_listbox']/li[3]"
    textbox_itemCode_xpath = "//input[@id='ItemCode']"
    textbox_itemName_id = "ItemName"
    textbox_itemDescription_xpath = "//input[@id='ItemDescription']"
    textbox_upcNumber_xpath = "//input[@id='UPCCode']"
    increase_value = '//*[@id="icform"]/div[8]/div[1]/span[2]/span/span[1]/span[1]/span'
    textbox_standardCost_name = "//*[@id='StandardCost']"
    textbox_sellingPrice_id = "UnitPrice"
    button_saveItem_id = 'btnContinueSave'

    #################### Edit Item Page Objects ############################
    textbox_searchItem_id = 'searchBox'
    button_search_id = 'searchBtn'
    link_searchItemValue_xpath = '//*[@id="kGrid"]/table/tbody/tr/td[2]/a'
    button_updateItem_xpath = '//*[@id="icform"]/div[18]/div/button[1]'

    #################### Serialized Item Page Objects ############################
    dropdown_itemType_xpath = '//*[@id="icform"]/div[2]/div[3]/span[2]/span/span[2]'
    dropdown_itemTypeValue_xpath = '//*[@id="ItemType_listbox"]/li[9]'
    dropdown_itemMake_xpath = '//*[@id="icform"]/div[5]/div[1]/span/span/span[2]'
    dropdown_makeValue_xpath = '//*[@id="sMake_listbox"]/li'
    dropdown_itemBrand_xpath = '//*[@id="icform"]/div[5]/div[2]/span/span/span[2]'
    dropdown_brandValue_xpath = '//*[@id="sBrand_listbox"]/li'
    dropdown_itemModel_xpath = '//*[@id="icform"]/div[5]/div[3]/span/span/span[2]'
    dropdown_modelValue_xpath = '//*[@id="sModel_listbox"]/li'
    button_addItemMemory_xpath = '//*[@id="icform"]/div[5]/div[4]/a/span[2]'
    textbox_addItemMemory_xpath = '//*[@id="sName"]'
    button_saveItemMemory_xpath = '//*[@id="btn_Submit"]/span[2]'
    dropdown_itemMemory_xpath = '//*[@id="icform"]/div[5]/div[4]/span/span/span[1]'
    textbox_searchItemMemory_xpath = '//*[@id="sCapacity-list"]/span/input'
    dropdown_memoryValue_xpath = '//*[@id="c511fa5f-7828-47ad-ad1d-f533c8515a02"]'

    def __init__(self, driver):
        self.driver = driver

    def clickInventoryNav(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, self.list_advanceInventory_linktxt).click()

    def clickItemMasterNav(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, self.link_itemMasterNav_linktxt).click()

    def clickAddItem(self):
        self.driver.find_element(By.XPATH, self.button_addItem_xpath).click()

    def selectItemCategory(self):
        self.driver.find_element(By.XPATH, self.dropdown_itemCategory_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.select_itemCategory_xpath).click()

    def enterItemCode(self, code):
        self.driver.find_element(By.XPATH, self.textbox_itemCode_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_itemCode_xpath).send_keys(code)

    def enterItemName(self, name):
        self.driver.find_element(By.ID, self.textbox_itemName_id).send_keys(name)

    def enterItemDescription(self, description):
        self.driver.find_element(By.XPATH, self.textbox_itemDescription_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_itemDescription_xpath).send_keys(description)

    def enterUPCNumber(self, upc):
        print(upc)
        self.driver.find_element(By.XPATH, self.textbox_upcNumber_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_upcNumber_xpath).send_keys(upc)

    # def enterStandardCost(self, stdCost):
    #     self.driver.find_element(By.XPATH, self.increase_value).click()
    #     self.driver.find_element(By.XPATH, self.increase_value).send_keys(stdCost)
    #
    # def enterSellingPrice(self, sellPrice):
    #     self.driver.find_element(By.ID, self.textbox_sellingPrice_id).click()
    #     self.driver.find_element(By.ID, self.textbox_sellingPrice_id).send_keys(sellPrice)

    def clickSaveAndContinue(self):
        self.driver.find_element(By.ID, self.button_saveItem_id).click()

    #################### Edit Item Action Functions ############################
    def searchItem(self, itemCode):
        self.driver.find_element(By.ID, self.textbox_searchItem_id).clear()
        self.driver.find_element(By.ID, self.textbox_searchItem_id).send_keys(itemCode)

    def clickSearchedButton(self):
        self.driver.find_element(By.ID, self.button_search_id).click()

    def clickSearchedItem(self):
        self.driver.find_element(By.XPATH, self.link_searchItemValue_xpath).click()

    def clickSaveAndClose(self):
        self.driver.find_element(By.XPATH, self.button_updateItem_xpath).click()

    def selectItemType(self):
       self.driver.find_element(By.XPATH, self.dropdown_itemType_xpath).click()
       time.sleep(2)
       self.driver.find_element(By.XPATH, self.dropdown_itemTypeValue_xpath).click()

    def selectItemMake(self):
        self.driver.find_element(By.XPATH, self.dropdown_itemMake_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.dropdown_makeValue_xpath).click()

    def selectItemBrand(self):
        self.driver.find_element(By.XPATH, self.dropdown_itemBrand_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.dropdown_brandValue_xpath).click()

    def selectItemModel(self):
        self.driver.find_element(By.XPATH, self.dropdown_itemModel_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.dropdown_modelValue_xpath).click()

    def addItemMemoryAtribute(self, memory):
        self.driver.find_element(By.XPATH, self.button_addItemMemory_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.textbox_addItemMemory_xpath).send_keys(memory)
        self.driver.find_element(By.XPATH, self.button_saveItemMemory_xpath).click()

    def selectItemMemory(self, memory):
        self.driver.find_element(By.XPATH, self.dropdown_itemMemory_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.textbox_searchItemMemory_xpath).send_keys(memory)
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.dropdown_memoryValue_xpath).click()
from selenium.webdriver.common.by import By


class itemSearch:
    list_advanceInventory_linktxt = "Advance Inventory"
    link_itemMasterNav_linktxt = 'Item Master'
    textbox_searchItem_id = 'searchBox'
    button_search_id = 'searchBtn'
    dropdown_itemsCount_xpath = '//*[@id="kGrid"]/div/span[1]/span/span/span[2]/span'
    value_itemCount_xpath = '//*[@id="htmlBody"]/div[8]/div/div[2]/ul/li[4]'
    table_xpath = '//*[@id="kGrid"]/table'
    table_row_xpath = '//*[@id="kGrid"]/table/tbody/tr'
    table_column_xpath = '//*[@id="kGrid"]/table/tbody/tr/td'

    def __init__(self, driver):
        self.flag = None
        self.driver = driver

    def clickInventoryNav(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, self.list_advanceInventory_linktxt).click()

    def clickItemMasterNav(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, self.link_itemMasterNav_linktxt).click()

    def searchItem(self, itemCode):
        self.driver.find_element(By.ID, self.textbox_searchItem_id).clear()
        self.driver.find_element(By.ID, self.textbox_searchItem_id).send_keys(itemCode)

    def clickSearchedButton(self):
        self.driver.find_element(By.ID, self.button_search_id).click()

    def setItemCount(self):
        self.driver.find_element(By.XPATH, self.dropdown_itemsCount_xpath).click()
        self.driver.find_element(By.XPATH, self.value_itemCount_xpath).click()

    def tableRowCount(self):
        return len(self.driver.find_elements(By.XPATH, self.table_row_xpath))

    def tableColumnCount(self):
        return len(self.driver.find_element(By.XPATH, self.table_column_xpath))

    def searchByItemName(self, itemName):
        flag = False
        for i in range(1, self.tableRowCount()+1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            name = table.find_element(By.XPATH, '//*[@id="kGrid"]/table/tbody/tr["+str(i)+"]/td[3]').text
            if name == itemName:
                flag = True
                break
        return flag



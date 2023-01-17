import time
from selenium.webdriver.common.by import By


class ItemManagement:
    list_advanceInventory_linktxt = "Advance Inventory"
    link_itemMasterNav_linktxt = 'Item Master'
    textbox_searchItem_id = 'searchBox'
    button_search_id = 'searchBtn'
    link_searchItemValue_xpath = '//*[@id="kGrid"]/table/tbody/tr/td[2]/a'
    button_updateItem_xpath = '//*[@id="icform"]/div[18]/div/button[1]'
    dropdown_itemsCount_xpath = '//*[@id="kGrid"]/div/span[1]/span/span/span[2]/span'
    value_itemCount_xpath = '//*[@id="kGrid"]/div/span[1]/span/select/option[4]'

    def __init__(self, driver):
        self.driver = driver


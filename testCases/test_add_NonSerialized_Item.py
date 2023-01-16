import random
import time
import string
import pytest
from selenium import webdriver
from pageObjects.manageItem import ItemManagement
from pageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen


class Test_003_Add_NonSerialized_Item:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_addNonSerializedItem(self, setup):
        self.logger.info("********** Test_003_Add_NonSerialized_Item **********")
        self.logger.info("********** Verifying Add Non-Serialized Item **********")

        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.lp.clickRemindLater()
        self.logger.info("********** Login Successful **********")

        self.ai = ItemManagement(self.driver)
        self.ai.clickInventoryNav()
        time.sleep(2)

        self.ai.clickItemMasterNav()
        time.sleep(2)

        self.ai.clickAddItem()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(10)


        # self.code = 'AT' + randomNumber()
        # print(self.code)
        # self.ai.enterItemCode(self.code)
        # time.sleep(2)
        #
        # self.name = 'AT Item ' + randomNumber()
        # print(self.name)
        # self.ai.enterItemName(self.name)
        # time.sleep(2)
        #
        # self.ai.enterItemDescription('This it the item created by automation testing. The test case id is '
        #                              'Test_003_Add_NonSerialized_Item')
        # # time.sleep(2)
        #
        # self.upc = 'UPC' + randomNumber()
        # print(self.upc)
        # self.ai.enterUPCNumber(self.upc)
        # time.sleep(2)

        self.ai.enterStandardCost(500)
        time.sleep(2)

        # self.ai.enterSellingPrice(1000)
        # time.sleep(2)
        #
        # self.ai.clickSaveAndContinue()
        # time.sleep(5)
        #
        # self.msg = self.driver.find_elements_by_tag_name("body").text
        #
        # if self.msg == 'Record Save Successfully':
        #     assert True
        # else:
        #     assert False

        # // *[ @ id = "htmlBody"] / div[3] / div / div / text()
        # // div[ @
        #
        # class ='k-notification-wrap']
        # // div[@ class ='k-notification-wrap']
        # Record Save Successfully

# def randomNumber():
#     randNum = ''.join(random.choice(string.digits) for i in range(5))
#     return randNum


# def randomChar():
#     randChar = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
#     return randChar

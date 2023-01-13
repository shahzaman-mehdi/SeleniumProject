import time
import pytest
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
        self.logger.info("********** Login Successfull **********")

        self.lp.clickRemindLater()
        self.ai = ItemManagement()
        self.ai.clickInventoryNav()
        self.ai.clickItemMasterNav()
        self.ai.clickAddItem()
        self.ai.clickCategoryLink()
        self.ai.selectItemCategoryValue()



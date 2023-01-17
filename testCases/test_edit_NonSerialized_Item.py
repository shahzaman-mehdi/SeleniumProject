import random
import time
import string
from selenium.webdriver.common.by import By
from pageObjects.manageItem import ItemManagement
from pageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen


class Test_004_Edit_NonSerialized_Item:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_editNonSerializedItem(self, setup):
        self.logger.info("********** Test_003_Edit_NonSerialized_Item **********")
        self.logger.info("********** Logging into ERP **********")

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
        self.logger.info("********** Opening Items List Screen **********")
        self.ai.clickInventoryNav()
        time.sleep(2)

        self.ai.clickItemMasterNav()
        self.logger.info("********** Items List Screen Appeared **********")
        time.sleep(2)

        self.logger.info("********** Searching Item **********")
        self.ai.searchItem("EDIT_NS_004_AT")
        time.sleep(5)

        self.logger.info("********** Opening searched item in edit view **********")
        self.ai.clickSearchedItem()
        time.sleep(2)

        self.logger.info("***** Updating the item description and UPC number field values *****")
        self.upc = 'UPC' + randomNumber()
        self.ai.enterUPCNumber(self.upc)
        time.sleep(2)

        self.ai.enterItemDescription("Description is updated by automated test of edit Non-Serialized item")
        time.sleep(2)

        self.ai.clickSaveAndClose()
        self.logger.info("***** Saving the updated item *****")

        time.sleep(5)

        self.msg = self.driver.find_element(By.TAG_NAME, 'body').text

        if 'Record Updated Successfully' in self.msg:
            assert True == True
            self.logger.info("**********Item updated successfully **********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test-editNonSerializedItem_scr.png")
            self.logger.error("**********Edit Non Serialized Item Test Failed **********")
            assert True == False


def randomNumber():
    randNum = ''.join(random.choice(string.digits) for i in range(5))
    return randNum

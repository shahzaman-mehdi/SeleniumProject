import time
from pageObjects.searchItem import itemSearch
from pageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen


class Test_004_Edit_NonSerialized_Item:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_searchItem(self, setup):
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

        self.si = itemSearch(self.driver)
        self.logger.info("********** Opening Items List Screen **********")
        self.si.clickInventoryNav()
        time.sleep(2)

        self.si.clickItemMasterNav()
        self.logger.info("********** Items List Screen Appeared **********")
        time.sleep(5)

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.si.setItemCount()
        time.sleep(3)

        self.logger.info("********** Searching Item **********")
        self.si.searchItem("EDIT_NS_004_AT")
        self.si.clickSearchedButton()
        time.sleep(5)

        status = self.si.searchByItemName('AT Edit Non Serialized Items')

        if status == True:
            assert True
            self.logger.info("********** Item search test passed **********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_searchItem-scr.png")
            self.logger.error("********** Item search test failed **********")
            assert False

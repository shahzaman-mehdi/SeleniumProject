import pytest

from pageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen



class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("********** Test_001_Login **********")
        self.logger.info("********** Verifying Login Test **********")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.lp.clickRemindLater()
        act_title = self.driver.title
        if act_title == "HomePage":
            self.logger.info("********** Login Test Passed **********")
            self.driver.close()
            assert True
        else:
            self.logger.error("********** Login Test Failed **********")
            self.driver.close()
            assert False

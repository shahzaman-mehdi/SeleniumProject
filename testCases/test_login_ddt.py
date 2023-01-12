import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from Utilities import XLUtils


class Test_002_DDT_Login():
    baseURL = ReadConfig.getApplicationURL()
    path = './/testData/loginData.xlsx'

    logger = LogGen.loggen()

    def test_login_ddt(self, setup):
        self.logger.info("********** Test_002_DDT_Login **********")
        self.logger.info("********** Verifying Login DDT Test **********")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        lst_status= []
        for r in range(2, self.rows + 1):
            self.username = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUsername(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            self.lp.clickRemindLater()
            time.sleep(5)

            act_title = self.driver.title()
            exp_title = 'Homepage'

            if act_title == exp_title:
                if self.exp == 'pass':
                    self.logger.info("********** Passed **********")
                    lst_status.append("Pass")
                elif self.exp == "fail":
                    self.logger.info("********** Failed **********")
                    lst_status.append("Fail")

            elif act_title != exp_title:
                if self.exp == 'pass':
                    self.logger.info("********** Failed **********")
                    lst_status.append("Fail")
                elif self.exp == "fail":
                    self.logger.info("********** Passed **********")
                    lst_status.append("Pass")

                print(lst_status)
        if "Fail" not in lst_status:
            self.logger.info("********** DDT Login Test Passed **********")
            self.driver.close()
            assert True
        else:
            self.logger.error("********** DDT Login Test Failed **********")
            self.driver.close()
            assert True

        self.logger.error("********** DDT Login Test Completed **********")





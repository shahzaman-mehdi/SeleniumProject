from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username_id = "UserName"
    textbox_password_id = "Password"
    button_Login_name = "action:Login"
    button_remindLater_linkText = "Remind Me Later"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.NAME, self.button_Login_name).click()

    def clickRemindLater(self):
        self.driver.find_element(By.LINK_TEXT, self.button_remindLater_linkText).click()
#
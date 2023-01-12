import pytest
import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations/config.ini")


class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url = config.get("common info", "baseURL")
        return url

    @staticmethod
    def getUserEmail():
        email = config.get("common info", "user-email")
        return email

    @staticmethod
    def getPassword():
        password = config.get("common info", "user-password")
        return password

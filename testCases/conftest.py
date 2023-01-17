import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
from selenium.webdriver.firefox.options import Options


# from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(service=Service(executable_path="C:/Drivers/chromedriver.exe"))
    elif browser == 'firefox':
        options = Options()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        driver = webdriver.Firefox(executable_path=r'C:\Drivers\geckodriver.exe', options=options)
    elif browser == 'edge':
        driver = webdriver.Edge(service=Service(executable_path="C:/Drivers/msedgedriver.exe"))
    elif browser == 'all':
        driver = webdriver.Chrome(service=Service(executable_path="C:/Drivers/chromedriver.exe"))
        options = Options()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        driver = webdriver.Firefox(executable_path=r'C:\Drivers\geckodriver.exe', options=options)
        driver = webdriver.Edge(service=Service(executable_path="C:/Drivers/msedgedriver.exe"))
    else:
        driver = webdriver.Chrome(service=Service(executable_path="C:/Drivers/chromedriver.exe"))
    return driver


def pytest_addoption(parser):  # Hook: This will get value from CLI
    parser.addoption("--browser")


@pytest.fixture
def browser(request):  # This will return the Browser value from cli to setup method
    return request.config.getoption("--browser")


################### Pytest HTML Report ################################

def pytest_configure(config):
    config._metadata['Project Name'] = 'Attendance Portal'
    config._metadata['Module Name'] = 'Login/Signup'
    config._metadata['Tester'] = 'Mehdi'

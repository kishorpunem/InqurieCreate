import time

from selenium.webdriver import Edge
from selenium.webdriver import firefox
from Library import ConfigReader
from selenium.webdriver.common.by import By


def startBrowser():
    global driver
    if((ConfigReader.readConfigData('Details','Browser'))=="Edge"):
        path = "./Driver/msedgedriver.exe"
        driver = Edge(executable_path=path)
    elif((ConfigReader.readConfigData('Details','Browser'))=="firefox"):
        path = "C:\\Users\\Kishor\\Downloads\\geckodriver-v0.31.0-win64 (1)\\geckodriver.exe"
        driver = firefox(executable_path=path)
    driver.get(ConfigReader.readConfigData('Details','Application_URL'))
    assert driver.current_url=="http://test.trukker.ae/"
    driver.maximize_window()
    time.sleep(5)
    return driver


def closeBrowser():
   driver.close()

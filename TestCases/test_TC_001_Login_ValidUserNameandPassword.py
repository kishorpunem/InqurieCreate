import time
from selenium.webdriver.common.by import By
from Library import ConfigReader


from Base import BaseFile


def test_ValidUserNameandPassword():
    driver = BaseFile.startBrowser()
    driver.find_element(By.ID, ConfigReader.fetchElementlocators("Login", "Login_button")).click()
    driver.find_element(By.ID, ConfigReader.fetchElementlocators("Login", "User_name")).send_keys(
        "srivani.koneti@trukker.com")
    driver.find_element(By.ID, ConfigReader.fetchElementlocators("Login", "Password_name")).send_keys("123")
    driver.find_element(By.ID, ConfigReader.fetchElementlocators("Login", "Login_Tap")).click()
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH,ConfigReader.fetchElementlocators("Login", "Inquire_button")).click()
    get_title = driver.title
    print(get_title)
    assert driver.title == "trukker"
    time.sleep(5)
    driver.find_element(By.XPATH,ConfigReader.fetchElementlocators("Login", "Add_New")).click()


    driver.close()

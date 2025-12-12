from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class MyAccountPage():

    lnk_logout_xpath = "//aside[@id='column-right']//a[normalize-space()='Logout']"

    def __init__(self, driver:WebDriver):
        self.driver = driver

    def clickLogout(self):
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH,self.lnk_logout_xpath).click()

from page_objects.HomePage import HomePage
from page_objects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import os
from utilities.screenshot_utils import *

class Test_Login():
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()  # Logger

    user = ReadConfig.getUseremail()
    password = ReadConfig.getpassword()

    def test_login(self,setup):
        self.logger.info("******* Starting test_002_login **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp=HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickLogin()

        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.user)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.targetpage=self.lp.isMyAccountPageExists()
        if self.targetpage==True:
            assert True
        else:
            headless_capture_full_page_screenshot(self.driver, "Login_test_headless.png")
            head_capture_full_page_screenshot(self.driver, "Login_test_head.png")
            assert False

        
        self.logger.info("******* End of test_002_login **********")

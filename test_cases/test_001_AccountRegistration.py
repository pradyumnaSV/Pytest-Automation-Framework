import pytest
from page_objects.HomePage import HomePage
from page_objects.AccountRegistrationPage import AccountRegistrationPage
from utilities.randomString import faker_generate_test_email
import os
from utilities.screenshot_utils import *
from utilities.readProperties import ReadConfig


from selenium.webdriver.remote.webdriver import WebDriver
from utilities.customLogger import LogGen


class Test_001_AccountReg:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen() 
    

    @pytest.mark.sanity
    def test_account_reg(self,setup: WebDriver):

        self.logger.info("**** account regestration is started*****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp=HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickRegister()
        self.regpage=AccountRegistrationPage(self.driver)

        self.regpage.setFirstName("John")
        self.regpage.setLastName("Canedy")
        #self.email = faker_generate_test_email()
        self.email = "vdvd334435@gmail.com"
        self.regpage.setEmail(self.email)
        self.regpage.setTelephone("65656565")
        self.regpage.setPassword("abcxyz")
        self.regpage.setConfirmPassword("abcxyz")
        self.regpage.setPrivacyPolicy()
        self.regpage.clickContinue()
        self.confmsg=self.regpage.getconfirmationmsg()
        
        if self.confmsg=="Your Account Has Been Created!":
            self.logger.info("**** Verification Successful: Account created ****")
            self.logger.info("**** account regestration is completed*****")
            assert True
        else:

            # 1. Use os.path.join to safely build the relative path
            relative_path = os.path.join(os.curdir, "screenshots", "test_ss.png")
            full_path = os.path.abspath(relative_path)
            self.driver.save_screenshot(full_path)

            headless_capture_full_page_screenshot(self.driver, "homepage_test_complete.png")
            head_capture_full_page_screenshot(self.driver, "homepage_test_complete1.png")

            
            self.logger.info("**** account regestration is completed (with failure)*****")
            assert False     
            







import os
from datetime import datetime
# Add this line at the very top
os.environ['WDM_SSL_VERIFY'] = '0'
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService

from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService

from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService


import time

def pytest_addoption(parser):
    """
    This hook adds custom command-line options to pytest.
    '--browser': Specifies the browser to use (chrome, firefox, edge).
    '--headless': A boolean flag to run the browser in headless mode.
    '--env': Specifies the environment (dev, sit, prod) to run against.
    """
    parser.addoption("--browser", action="store", help="Specify browser: chrome, firefox, or edge")
    

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")



@pytest.fixture(scope="function")
def setup(browser):

    if browser == 'edge':
        service_obj = EdgeService(EdgeChromiumDriverManager().install())
        options = EdgeOptions()
        
        # Pass the service object to the driver
        driver = webdriver.Edge(service=service_obj, options=options)

    elif browser == 'chrome':
        # Create a Service object with the path from ChromeDriverManager
        service_obj = ChromeService(ChromeDriverManager().install())
        options = ChromeOptions()
        options.add_argument("--headless")  # <--- THIS IS THE KEY
        
        # Pass the service object to the driver
        driver = webdriver.Chrome(service=service_obj, options=options)

    elif browser == 'firefox':
        service_obj = FirefoxService(GeckoDriverManager().install())
        options = FirefoxOptions()
        
        # Pass the service object to the driver
        driver = webdriver.Firefox(service=service_obj, options=options)

    else:

        service_obj = ChromeService(ChromeDriverManager().install())
        options = ChromeOptions()
        # options.add_argument("--headless")  # <--- THIS IS THE KEY
        
        # Pass the service object to the driver
        driver = webdriver.Chrome(service=service_obj, options=options)
    
    
    yield driver

    time.sleep(20)

    driver.quit()



#################### pytest HTML report##########

# ------------------------------------------------------------------------------------
# SECTION 2: PYTEST-HTML REPORT CUSTOMIZATION HOOKS
# (This section is unchanged and correct)
# ------------------------------------------------------------------------------------

########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Opencart'
    config._metadata['Module Name'] = 'CustRegistration'
    config._metadata['Tester'] = 'Pavan'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

#Specifying report folder location and save report with timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(os.curdir)+"\\reports\\"+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"



# (gitpytestenv) C:\Users\svpra\OneDrive\Desktop\Git_projects\git_pytest_project>
# pytest -s -v --capture=tee-sys .\\test_cases
# --capture=tee-sys to capture logs on failure


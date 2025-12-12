from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# 1. Setup - Automatically downloads and sets up the correct driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# 2. Open URL
driver.get("https://naveenautomationlabs.com/opencart/index.php?route=product/category&path=20")

# 3. Find elements and perform actions
# Note: Added an implicit wait is recommended here as the page loads dynamically
driver.implicitly_wait(20) 

time.sleep(10)

# 6. Close the browser
driver.quit() # quit() is generally preferred over close() to kill the process completely
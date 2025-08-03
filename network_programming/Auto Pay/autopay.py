# In progress

import os
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

debug = True
load_dotenv()

LOGIN_PAGE = os.getenv('LOGIN_PAGE')
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')

options = Options()

if debug:
    options.add_experimental_option("detach", True)
    options.add_argument("--auto-open-devtools-for-tabs")
else:
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")

driver = webdriver.Edge(
    service=Service(ChromeDriverManager().install()),
    options=options
    )
driver.get("https://www.google.com")

user_input = driver.find_element(By.ID, "user-name")

if user_input:
    user_input.send_keys("12345")

if debug:
    print("Running in debug mode - browser will stay open.")
else:
    driver.quit()




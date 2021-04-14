from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome("C:\exe\chromedriver_win32\chromedriver")
driver.get("https://web.whatsapp.com")
wait = webDriverWait(driver, 600)

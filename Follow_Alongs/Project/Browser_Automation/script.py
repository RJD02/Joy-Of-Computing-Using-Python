from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("C:\exe\chromedriver_win32\chromedriver")
driver.get("https://web.whatsapp.com")
wait = WebDriverWait(driver, 600)
target = '"Soumya Dulange"' # Name of the target friend
string = "Sent using python" # Message you want to send
x_arg = "//span[contains(@title, " + target + ")]"
target = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
target.click()


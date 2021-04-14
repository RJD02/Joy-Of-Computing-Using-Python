from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("C:\exe\chromedriver_win32\chromedriver")
driver.get("https://web.whatsapp.com")
wait = WebDriverWait(driver, 300)
target = ['"Soumya Dulange"', '"Dulange😁😁😁"'] # Name of the target friend
target_names = ['Soumya Dulange', 'Everybody in Dulange']
count = 0
for name in target:
    x_arg = "//span[contains(@title, " + name + ")]"
    name_wait = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
    name_wait.click()
    string = "Hello " + target_names[count] + " This message is for you" # Message you want to send
    input_box = driver.find_element_by_class_name("_2A8P4")
    #  for i in range(5):
    input_box.send_keys(string + Keys.ENTER)
    count += 1

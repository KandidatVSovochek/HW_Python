import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService
                           (GeckoDriverManager().install()))
driver.implicitly_wait(10)
driver.get("http://the-internet.herokuapp.com/inputs")
find_field = "input"
input_text = driver.find_element(By.CSS_SELECTOR, find_field)
input_text.send_keys("Sky")
time.sleep(3)
input_text.clear()
time.sleep(2)
input_text.send_keys("Pro")
driver.quit()

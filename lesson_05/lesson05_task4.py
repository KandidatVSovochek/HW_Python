from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService
                           (GeckoDriverManager().install()))
driver.implicitly_wait(10)
driver.get("http://the-internet.herokuapp.com/login")
find_username = "#username"
input_username = driver.find_element(By.CSS_SELECTOR, find_username)
input_username.send_keys("tomsmith")
find_password = "#password"
input_password = driver.find_element(By.CSS_SELECTOR, find_password)
input_password.send_keys("SuperSecretPassword!")
login = driver.find_element(By.CSS_SELECTOR, ".radius").click()
green_field = driver.find_element(By.CSS_SELECTOR, "#flash").text
print(green_field)
driver.quit()

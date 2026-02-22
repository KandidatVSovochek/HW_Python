from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService
                          (ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("http://uitestingplayground.com/textinput/")
input_field = ".form-control"
input_text = driver.find_element(By.CSS_SELECTOR, input_field)
input_text.send_keys("SkyPro")
button = ".btn-primary"
button_element = driver.find_element(By.CSS_SELECTOR, button).click()
new_button = driver.find_element(By.CSS_SELECTOR, button).text
print(new_button)
driver.quit()

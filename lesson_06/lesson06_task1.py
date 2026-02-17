from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService
                          (ChromeDriverManager().install()))
driver.implicitly_wait(50)
driver.get("http://uitestingplayground.com/ajax/")
button = ".btn-primary"
button = driver.find_element(By.CSS_SELECTOR, button).click()
element = "p.bg-success"
element = driver.find_element(By.CSS_SELECTOR, element).text
print(element)
driver.quit()

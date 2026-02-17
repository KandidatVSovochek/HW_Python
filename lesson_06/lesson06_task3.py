from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService
                          (ChromeDriverManager().install()))
driver.implicitly_wait(10)
base_url = "https://bonigarcia.dev"
driver.get(f"{base_url}/selenium-webdriver-java/loading-images.html")
element = WebDriverWait(driver, 40).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#landscape"))
    )
pic_selector = "#award"
src = driver.find_element(By.CSS_SELECTOR, pic_selector).get_attribute("src")
print(src)
driver.quit()

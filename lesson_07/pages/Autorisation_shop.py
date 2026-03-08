from selenium.webdriver.common.by import By


class Autorisation:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com")
        self.driver.implicitly_wait(10)

    def log_pass(self):
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")

    def login_button(self):
        self.driver.find_element(By.ID, "login-button").click()

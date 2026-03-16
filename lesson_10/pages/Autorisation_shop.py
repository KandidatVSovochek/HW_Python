import allure
from selenium.webdriver.common.by import By


class Autorisation:

    @allure.step("api.Перейти на сайт {url}")
    def __init__(self, driver, url="https://www.saucedemo.com"):
        self.driver = driver
        self.driver.get(url)
        self.driver.implicitly_wait(10)

    @allure.step("Авторизация {user}:{password}")
    def log_pass(self, user="standard_user", password="secret_sauce"):
        self.driver.find_element(By.ID, "user-name").send_keys(user)
        self.driver.find_element(By.ID, "password").send_keys(password)

    @allure.step("Нажатие кнопки подтверждения входа")
    def login_button(self):
        self.driver.find_element(By.ID, "login-button").click()

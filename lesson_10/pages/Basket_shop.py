import allure
from selenium.webdriver.common.by import By


class Basket:

    def __init__(self, browser):
        self.driver = browser

    @allure.step("Переход к оформлению заказа")
    def checkout_button(self):
        self.driver.find_element(By.ID, "checkout").click()

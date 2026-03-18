import allure
from selenium.webdriver.common.by import By


class MainPage:

    def __init__(self, browser):
        self.driver = browser

    @allure.step("Выбор товаров")
    def add_item(self):
        """
            Добавлене товаров в корзину.
            :return: None
        """
        self.driver.find_element(By.ID,
                                 "add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.ID,
                                 "add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(By.ID,
                                 "add-to-cart-sauce-labs-onesie").click()

    @allure.step("Переход в корзину")
    def to_basket(self):
        """
            Функция нажимает на указанную кнопку корзины.
            :return: None
        """
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".shopping_cart_link").click()

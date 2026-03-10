from selenium.webdriver.common.by import By


class MainPage:

    def __init__(self, browser):
        self.driver = browser

    def add_item(self):
        self.driver.find_element(By.ID,
                                 "add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.ID,
                                 "add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(By.ID,
                                 "add-to-cart-sauce-labs-onesie").click()

    def to_basket(self):
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".shopping_cart_link").click()

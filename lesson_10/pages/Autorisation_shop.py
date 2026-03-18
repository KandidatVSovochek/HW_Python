import allure
from selenium.webdriver.common.by import By


class Autorisation:

    @allure.step("api.Перейти на сайт {url}")
    def __init__(self, driver, url: str = "https://www.saucedemo.com"):
        """
            Эта функция нужна чтобы перейти на сайт интеренет магазина.
            Функция берет значение url и отправляет запрос на указанный адрес.
            :url: str
            :return: None
        """
        self.driver = driver
        self.driver.get(url)
        self.driver.implicitly_wait(10)

    @allure.step("Авторизация {user}:{password}")
    def log_pass(self, user: str = "standard_user",
                 password: str = "secret_sauce"):
        """
            Эта функция берет значение user и password и
            подставляет их в указанные поля.
            :user: str
            :password: str
            :return: None
        """
        self.driver.find_element(By.ID, "user-name").send_keys(user)
        self.driver.find_element(By.ID, "password").send_keys(password)

    @allure.step("Нажатие кнопки подтверждения входа")
    def login_button(self):
        """
            Функция нажимает на указанную кнопку авторизации.
            :return: None
        """
        self.driver.find_element(By.ID, "login-button").click()

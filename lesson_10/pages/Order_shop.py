import allure
from selenium.webdriver.common.by import By


class Order:

    def __init__(self, browser):
        self.driver = browser

    @allure.step("Оформление заказа используя {fname}. {lname}. {ind}")
    def making_an_order(self, fname: str = "Катя", lname: str = "Мельникова",
                        ind: str = "123456"):
        """
            Эта функция берет значение fname, lname и ind
            и подставляет их в указанные поля.
            :fname: str
            :lname: str
            :ind: str
            :return: None
        """
        self.driver.find_element(By.ID, "first-name").send_keys(fname)
        self.driver.find_element(By.ID, "last-name").send_keys(lname)
        self.driver.find_element(By.ID, "postal-code").send_keys(ind)
        self.driver.find_element(By.ID, "continue").click()

    @allure.step("Проверка итоговой цены")
    def check_count(self):
        """
            Эта функция проверяет равно ли сумма заказа
            в найденном поле на сайте сумме в условии.
            :return: None
        """
        total = self.driver.find_element(By.CSS_SELECTOR,
                                         ".summary_total_label").text
        assert "Total: $58.29" in total
        print(total)

    def close(self):
        self.driver.quit()

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Calc:

    def __init__(self, driver):
        self.driver = driver
        base_url = "https://bonigarcia.dev/selenium-webdriver-java"
        self.driver.get(f"{base_url}/slow-calculator.html")
        self.driver.implicitly_wait(10)

    def delay(self):
        """
            Указание интеревала ожидания ответа.
            :return: None
        """
        self.driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        self.driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(45)

    def count(self):
        """
            Написание выражения для вычисления нажатием на кнопки.
            :return: None
        """
        self.driver.find_element(By.XPATH, "//span[text()='7']").click()
        self.driver.find_element(By.XPATH, "//span[text()='+']").click()
        self.driver.find_element(By.XPATH, "//span[text()='8']").click()
        self.driver.find_element(By.XPATH, "//span[text()='=']").click()

    def result(self):
        """
            Эта функция проверяет равно ли значение вычисления указанное
            в найденном поле на сайте значинию в условии.
            :return: None
        """
        WebDriverWait(self.driver, 45).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), "15"))
        actual_answer = self.driver.find_element(By.CSS_SELECTOR,
                                                 ".screen").text
        assert actual_answer == "15"

    def close(self):
        self.driver.quit()

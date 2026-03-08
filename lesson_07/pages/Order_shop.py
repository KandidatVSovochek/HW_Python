from selenium.webdriver.common.by import By


class Order:

    def __init__(self, browser):
        self.driver = browser

    def making_an_order(self):
        self.driver.find_element(By.ID, "first-name").send_keys("Катя")
        self.driver.find_element(By.ID, "last-name").send_keys("Мельникова")
        self.driver.find_element(By.ID, "postal-code").send_keys("123456")
        self.driver.find_element(By.ID, "continue").click()

    def check_count(self):
        total = self.driver.find_element(By.CSS_SELECTOR,
                                         ".summary_total_label").text
        assert "Total: $58.29" in total
        print(total)

    def close(self):
        self.driver.quit()

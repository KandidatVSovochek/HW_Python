from calc import Calc
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_calc():
    driver = webdriver.Chrome()
    calc = Calc(driver)
    calc.delay()
    calc.count()
    calc.result()
    actual_answer = driver.find_element(By.CSS_SELECTOR,
                                        ".screen").text
    assert actual_answer == "15"
    calc.close()

from calc import Calc
from selenium import webdriver


def test_calc():
    driver = webdriver.Chrome()
    calc = Calc(driver)
    calc.delay()
    calc.count()
    calc.result()
    calc.close()

import allure
from calc import Calc
from selenium import webdriver


@allure.title("Работа калькулятора")
@allure.description("Вычисление и проверка значения")
@allure.feature("API")
@allure.severity("critical")
def test_calc():
    with allure.step("Перейти на сайт калькулятора"):
        driver = webdriver.Chrome()
        calc = Calc(driver)
    with allure.step("Установить интервал ожидания ответа"):
        calc.delay()
    with allure.step("Написания выражения"):
        calc.count()
    with allure.step("Проверка результата"):
        calc.result()
    calc.close()

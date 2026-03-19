import allure
from pages.Autorisation_shop import Autorisation
from pages.Mainpage_shop import MainPage
from pages.Basket_shop import Basket
from pages.Order_shop import Order
from selenium import webdriver


@allure.title("Оформление заказа в интернет-магазине")
@allure.description("Оформление заказа в интеренет-магазине")
@allure.feature("API")
@allure.severity("critical")
def test_order_shop():
    with allure.step("Открыть страницу браузера"):
        driver = webdriver.Firefox()
    with allure.step("Авторизация"):
        autorisation = Autorisation(driver)
        autorisation.log_pass()
        autorisation.login_button()
    with allure.step("Добавление тавара в корзину на главной странице"):
        main_page = MainPage(driver)
        main_page.add_item()
    with allure.step("Перейти в корзину"):
        main_page.to_basket()
        basket = Basket(driver)
        basket.checkout_button()
    with allure.step("Оформленеи заказа"):
        order = Order(driver)
        order.making_an_order()
    with allure.step("Проверка суммы заказа"):
        order.check_count()
    order.close()

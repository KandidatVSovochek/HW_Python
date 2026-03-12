from pages.Autorisation_shop import Autorisation
from pages.Mainpage_shop import MainPage
from pages.Basket_shop import Basket
from pages.Order_shop import Order
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_order_shop():
    driver = webdriver.Firefox()
    autorisation = Autorisation(driver)
    autorisation.log_pass()
    autorisation.login_button()
    main_page = MainPage(driver)
    main_page.add_item()
    main_page.to_basket()
    basket = Basket(driver)
    basket.checkout_button()
    order = Order(driver)
    order.making_an_order()
    total = driver.find_element(By.CSS_SELECTOR,
                                ".summary_total_label").text
    assert "Total: $58.29" in total
    print(total)
    order.close()

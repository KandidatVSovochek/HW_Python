import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# @pytest.fixture()
# def driver():
#     service = ChromeService(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service)


@pytest.fixture()
def driver():
    service = EdgeService(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_edge_browser(driver):
    base_url = "https://bonigarcia.dev"
    driver.get(f"{base_url}/selenium-webdriver-java/data-types.html")
    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "zip-code").send_keys("")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    zip_field = driver.find_element(By.ID, "zip-code")
    color_zip_field = zip_field.value_of_css_property("background-color")
    expected_red = "rgba(248, 215, 218, 1)"
    assert color_zip_field == expected_red

    green_fields_names = ["first-name", "last-name", "address",
                          "e-mail", "phone", "city", "country",
                          "job-position", "company"]
    for field_id in green_fields_names:
        element = driver.find_element(By.ID, field_id)
        color_field = element.value_of_css_property("background-color")
        expected_green = "rgba(209, 231, 221, 1)"
        assert color_field == expected_green
    print("успешно")

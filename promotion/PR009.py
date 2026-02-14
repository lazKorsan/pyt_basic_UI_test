# PR009.py
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains

from pages.loginPage import login_method
from properties import test_data

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_promotion(driver):
    driver.get(test_data.login_url)
    login_method(driver, test_data.login_mail, test_data.instructor_password)

    # //*[@id="panel-sidebar-scroll"]
    DASHBOARD_XPATH = '//*[@id="panel-sidebar-scroll"]'
    dasbord_menu_Button = driver.find_element("xpath", DASHBOARD_XPATH)
    print(1)

    actions = ActionChains(driver)
    actions.move_to_element(dasbord_menu_Button).perform()
    print(2)

    # Elementin rengini yeşil yapma
    driver.execute_script("arguments[0].style.backgroundColor = 'green';", dasbord_menu_Button)
    print(3)

    # Merkezde kırmızı nokta ekleme
    driver.execute_script("""
            var dot = document.createElement('div');
            dot.style.width = '10px';
            dot.style.height = '10px';
            dot.style.backgroundColor = 'red';
            dot.style.borderRadius = '50%';
            dot.style.position = 'absolute';
            dot.style.top = (arguments[0].offsetTop + arguments[0].offsetHeight / 2 - 5) + 'px';
            dot.style.left = (arguments[0].offsetLeft + arguments[0].offsetWidth / 2 - 5) + 'px';
            document.body.appendChild(dot);
        """, dasbord_menu_Button)
    print(4)
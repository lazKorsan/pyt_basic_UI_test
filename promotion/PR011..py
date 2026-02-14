# PR009.py
import pytest
from selenium import webdriver
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

# PR009.py
import time

import pytest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pages.loginPage import login_method
from properties import test_data
from utils.click_utils import click_utils
from utils.hoover_utils import HoverUtils
from pages.promotionPage import promotionPages


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_promotion(driver):
    driver.get(test_data.login_url)
    login_method(driver, test_data.login_mail, test_data.instructor_password)

    hover_utils = HoverUtils(driver)
    hover_utils.hover_and_style(
        xpath='//*[@id="panel-sidebar-scroll"]',
        element_color='green',
        center_color='red'
    )

    # //*[@href="#marketingCollapse"]
    # '//*[@id="panel-sidebar-scroll"]/div[1]/div[2]/div/div/div/li[9]/a/span[2]'

    MARKETINGBUTTON_XPATH = '//*[@href="#marketingCollapse"]'
    marketing_Button = driver.find_element(By.XPATH, MARKETINGBUTTON_XPATH)
    actions = ActionChains(driver)
    actions.move_to_element(marketing_Button).perform()
    driver.execute_script("arguments[0].style.border='3px solid blue'", marketing_Button)
    marketing_Button.click()
    time.sleep(1)




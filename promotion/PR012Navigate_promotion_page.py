import time
import pytest
import select
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.loginPage import login_method
from properties import test_data
from utils.click_utils import click_utils
from pages.promotionPage import PromotionPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_promotion(driver):
    # Giriş sayfasına git
    driver.get(test_data.login_url)
    login_method(driver, test_data.login_mail, test_data.instructor_password)
    time.sleep(3)

    # Promosyon sayfasına git
    driver.get("https://qa.instulearn.com/panel/marketing/promotions")

    # Promosyon butonuna tıkla
    click_utils(driver, PromotionPage.GOLDPROMOTIONS_XPATH)
    time.sleep(1)

    # Kurs seçeneğini aç
    click_utils(driver, PromotionPage.SELECTCOURSEOPTIONS_XPATH)
    time.sleep(2)

    select_element = driver.find_elements(By.XPATH, PromotionPage.SELECTCOURSEOPTIONS_XPATH)
    select.select_by_value('3662')
    # Kurs seçeneğini seç


    # Ödeme butonuna tıkla
    click_utils(driver, PromotionPage.PAYBUTTON_XPATH)
    time.sleep(2)

# PR012Navigate_promotion_page.py
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from pages.loginPage import login_method
from properties import test_data
from utils import dom_hunter
from utils.dom_hunter import save_html_to_file


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_promotion(driver):
    driver.get(test_data.login_url)
    login_method(driver, test_data.login_mail, test_data.instructor_password)
    time.sleep(3)

    driver.get("https://qa.instulearn.com/panel/marketing/promotions")

    GOLDPROMOTIONS_XPATH = '//button[@data-promotion-id="2"]'
    driver.find_element("xpath", GOLDPROMOTIONS_XPATH).click()
    time.sleep(1)

    SELECTCOURSEOPTIONS_XPATH = '(//select[@name="webinar_id"])[2]'
    driver.find_element("xpath", SELECTCOURSEOPTIONS_XPATH).click()
    time.sleep(2)

    file_path = "C:/Users/user/PycharmProjects/behaveFeature/reports/page_source3.html"

    # ARTIK KARIŞIKLIK OLMAYACAK:
    # Kendi aktif driver'ımızı ve kayıt yolunu gönderiyoruz.
    save_html_to_file(driver, file_path)

    print("HTML başarıyla kaydedildi.")
    # driver.quit() # İsterseniz kapatabilirsiniz



import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from pages.loginPage import login_method
from pages.promotionPage import PromotionPage
from properties import test_data
from utils.click_utils import click_utils


class PromotionTest:
    def __init__(self, driver):
        self.driver = driver

    def mark_element(self, element):
        # Elementin üzerine kırmızı nokta koyar (Görsel kontrol için)
        driver = self.driver
        driver.execute_script("""
        var element = arguments[0];
        var rect = element.getBoundingClientRect();
        var d = document.createElement('div');
        d.style.position = 'fixed';
        d.style.left = (rect.left + rect.width/2) + 'px';
        d.style.top = (rect.top + rect.height/2) + 'px';
        d.style.width = '10px';
        d.style.height = '10px';
        d.style.background = 'red';
        d.style.borderRadius = '50%';
        d.style.zIndex = '10000';
        d.style.pointerEvents = 'none';
        document.body.appendChild(d);
        """, element)

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

    # Promosyon butonuna tıkla (Modalı açar)
    click_utils(driver, PromotionPage.GOLDPROMOTIONS_XPATH)
    time.sleep(2) # Modalin animasyonu için bekleme

    # Kurs seçimi problemi çözümü:
    # Standart select elementlerinde koordinata tıklamak (offset click) genellikle işe yaramaz 
    # çünkü açılan liste DOM'un farklı bir katmanında veya işletim sistemi kontrolündedir.
    # Ayrıca SweetAlert gibi modallar z-index ile katman oluşturur.
    # En garantili çözüm JavaScript ile değeri doğrudan atamaktır (Hile yöntemi).

    select_xpath = '(//select[@name="webinar_id"])[2]'
    select_element = driver.find_element("xpath", select_xpath)
    
    # Görsel olarak nereye işlem yapıldığını görmek için işaretleyelim
    pt = PromotionTest(driver)
    pt.mark_element(select_element)
    
    # JavaScript ile seçimi yap ve 'change' olayını tetikle
    driver.execute_script("arguments[0].value = '3662'; arguments[0].dispatchEvent(new Event('change'));", select_element)
    time.sleep(2)

    # Ödeme butonuna tıklama
    # Modal içindeki Pay butonu (2. sırada çünkü ilki gizli şablonda)
    pay_button_xpath = '(//button[contains(@class, "js-submit-promotion")])[2]'
    pay_button = driver.find_element("xpath", pay_button_xpath)
    
    # Butona da işaret koyalım
    pt.mark_element(pay_button)
    
    pay_button.click()
    time.sleep(5)  # Ödeme işlemi ve yönlendirme için bekleme süresi
import time
from selenium import webdriver
from utils.click_utils import click_utils

class PromotionPage:
    MARKETINGBUTTON_XPATH = '//*[@href="#marketingCollapse"]'
    GOLDPROMOTIONS_XPATH = '//button[@data-promotion-id="2"]'
    SELECTCOURSEOPTIONS_XPATH = '(//select[@name="webinar_id"])[2]'
    COURSE_OPTION_XPATH = '//option[@value="3662"]'
    PAYBUTTON_XPATH = '(//button[@class="btn btn-sm btn-primary js-submit-promotion"])[2]'

    driver = webdriver.Chrome()  # Doğru kullanım
    driver.maximize_window()

def promotion_pay(driver):
    from promotion.PR016DynamicModal import PromotionTest  # Import burada yapılır

    # Promosyon sayfasına git
    driver.get("https://qa.instulearn.com/panel/marketing/promotions")

    # Promosyon butonuna tıkla (Modalı açar)
    click_utils(driver, PromotionPage.GOLDPROMOTIONS_XPATH)
    time.sleep(2)  # Modalin animasyonu için bekleme

    # Kurs seçimi problemi çözümü:
    select_xpath = '(//select[@name="webinar_id"])[2]'
    select_element = driver.find_element("xpath", select_xpath)

    # Görsel olarak nereye işlem yapıldığını görmek için işaretleyelim
    pt = PromotionTest(driver)
    pt.mark_element(select_element)

    # Dinamik yaklaşım: Kurs ID'sini bir değişkene atayalım.
    target_course_id = '3662'

    # JavaScript ile seçimi yap ve 'change' olayını tetikle
    driver.execute_script(
        f"arguments[0].value = '{target_course_id}'; arguments[0].dispatchEvent(new Event('change'));",
        select_element)
    time.sleep(2)

    # Ödeme butonuna tıklama
    pay_button_xpath = '(//button[contains(@class, "js-submit-promotion")])[2]'
    pay_button = driver.find_element("xpath", pay_button_xpath)

    # Butona da işaret koyalım
    pt.mark_element(pay_button)

    pay_button.click()
    time.sleep(5)  # Ödeme işlemi ve yönlendirme için bekleme süresi

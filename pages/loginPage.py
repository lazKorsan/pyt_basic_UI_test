# loginPage.py
import time
from selenium.webdriver.common.by import By
from utils.click_utils import click_utils
from utils.sendkey_utils import sendKey_utils

MAILBOX_ID = (By.ID, "email")
PASSWORDBOX_ID = (By.ID, "password")
LOGINBUTTON_XPATH='//button[@class="btn btn-primary btn-block mt-20"]'

"""Verilen URL'ye giderek giriş sayfasını açar."""
def login_page(driver, url):

    driver.get(url)
    driver.maximize_window()
    time.sleep(1)

"""Giriş işlemi için e-posta ve şifre bilgilerini girer ve butona tıklar."""
def login_method(driver, mail, password):

    # Mail kutusuna e-posta adresini gir
    sendKey_utils(driver, MAILBOX_ID, mail)
    time.sleep(1)

    # Şifre kutusuna şifreyi gir
    sendKey_utils(driver, PASSWORDBOX_ID, password)
    time.sleep(1)

    # Giriş butonuna tıkla
    click_utils(driver, LOGINBUTTON_XPATH)

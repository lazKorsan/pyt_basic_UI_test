from selenium import webdriver






from datetime import datetime
import time

from utils.click_utils import click_utils
from utils.sendkey_utils import sendKey_utils

# GERÇEK LOCATOR'LAR
USERTYPESBUTTON_XPATH = "(//label[@class='font-12 cursor-pointer px-15 py-10'])[2]"
MAIL_BOX_ID = "//input[@class='form-control ']"
NAMEBOX_XPATH = '//input[@name="full_name"]'
PASSWORDBOX_XPATH = '//input[@id="password"]'
COMFIRMPASSWORDBOX_XPATH = '//input[@id="confirm_password"]'
SIGNIN2BUTTON_XPATH = '//button[@class="btn btn-primary btn-block mt-20"]'


def generate_dynamic_mail(prefix="lazKorsan"):
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"{prefix}{now}@gmail.com"


def register_method(driver, name, password):
    # user type seç
    click_utils(driver, USERTYPESBUTTON_XPATH)
    time.sleep(2)

    # mail üret
    email = generate_dynamic_mail()
    print(f"📧 Mail: {email}")

    # alanları doldur
    sendKey_utils(driver, MAIL_BOX_ID, email)
    time.sleep(1)

    sendKey_utils(driver, NAMEBOX_XPATH, name)
    time.sleep(1)

    sendKey_utils(driver, PASSWORDBOX_XPATH, password)
    time.sleep(1)

    sendKey_utils(driver, COMFIRMPASSWORDBOX_XPATH, password)
    time.sleep(1)

    # terms kabul
    driver.execute_script("document.getElementById('term').checked = true;")
    print("✅ Terms kabul edildi")

    time.sleep(1)

    # register
    click_utils(driver, SIGNIN2BUTTON_XPATH)
    time.sleep(3)

    return email

from pygments.styles.dracula import *
from datetime import datetime


from selenium import webdriver
import time

from pages import registerPage
from properties import test_data
from properties.test_data import *
from utils.click_utils import click_utils
from utils.sendkey_utils import sendKey_utils

# WebDriver'ı başlat
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(register_URL)

click_utils(
    driver,
    registerPage.USERTYPESBUTTON_XPATH,
)

time.sleep(2)

now = datetime.now().strftime("%Y%m%d%H%M%S")
instructor_mail = f"lazKorsan{now}@gmail.com"
print(instructor_mail)


sendKey_utils(
    driver,
    registerPage.MAIL_BOX_ID,
    instructor_mail,
)
time.sleep(1)

sendKey_utils(
    driver,
    registerPage.NAMEBOX_XPATH,
    test_data.instructor_name,
)
time.sleep(1)

sendKey_utils(
    driver,
    registerPage.PASSWORDBOX_XPATH,
    test_data.instructor_password,
)
time.sleep(1)

sendKey_utils(
    driver,
    registerPage.COMFIRMPASSWORDBOX_XPATH,
    test_data.instructor_password,
)
time.sleep(1)

driver.execute_script("document.getElementById('term').checked = true;")
print("✅ Terms kabul edildi")


time.sleep(1)

click_utils(
    driver,
    registerPage.SIGNIN2BUTTON_XPATH,
)

time.sleep(3)

# testdata veri aldı.
# pages clasddan veri aldı.


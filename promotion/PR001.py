import time

from selenium import webdriver

from pages import loginPage
from properties import test_data
from utils.click_utils import click_utils
from utils.dom_hunter import save_html_to_file
from utils.sendkey_utils import sendKey_utils


# login_page(driver,url)
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(test_data.login_url)

#### /////
# mail kutusuna ınstructorMail gir

# buradan başlayarak

#login_method(driver,mail,password)
sendKey_utils(
    driver,
    loginPage.MAILBOX_ID,
    test_data.login_mail,
)
time.sleep(1)

# password kutusuna password gir
sendKey_utils(
    driver,
    loginPage.PASSWORDBOX_ID,
    test_data.instructor_password
)
time.sleep(1)

# login butonuna tıkla

click_utils(
    driver,
    loginPage.LOGINBUTTON_XPATH
)



#### /////

from selenium import webdriver

from pages.loginPage import *
from properties import test_data
from utils.dom_hunter import save_html_to_file

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(test_data.login_url)
login_method(driver, test_data.login_mail, test_data.instructor_password)


file_path = r"C:\Users\user\PycharmProjects\behaveFeature\reports\page_source2.html"
save_html_to_file(file_path)
html_content = driver.page_source
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(html_content)
    file_path = r"C:\Users\user\PycharmProjects\behaveFeature\reports\page_source2.html"
    save_html_to_file(file_path)






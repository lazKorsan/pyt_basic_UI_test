from selenium import webdriver
from properties import test_data
from pages.loginPage import login_page, login_method

driver = webdriver.Chrome()
login_page(driver, test_data.login_url)
login_method(driver, test_data.login_mail, test_data.instructor_password)

from selenium import webdriver
from pages.registerPage import register_method
from properties.test_data import instructor_name, instructor_password, register_URL

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(register_URL)

email = register_method(
    driver,
    instructor_name,
    instructor_password
)

print(f"✅ Register tamamlandı -> {email}")

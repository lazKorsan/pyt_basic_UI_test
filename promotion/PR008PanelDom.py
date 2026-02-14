# PR008PanelDom.py
from selenium import webdriver
import time
from pages.loginPage import login_method # Kaynaktaki metod [1]
from properties import test_data
from utils.dom_hunter import save_html_to_file

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(test_data.login_url)

# Kaynak [1]'deki gibi driver'ı metoda paslıyoruz
login_method(driver, test_data.login_mail, test_data.instructor_password)

# Kayıt yolu
file_path = "C:/Users/user/PycharmProjects/behaveFeature/reports/page_source2.html"

# ARTIK KARIŞIKLIK OLMAYACAK:
# Kendi aktif driver'ımızı ve kayıt yolunu gönderiyoruz.
save_html_to_file(driver, file_path)

print("HTML başarıyla kaydedildi.")
# driver.quit() # İsterseniz kapatabilirsiniz

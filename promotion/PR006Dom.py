import time

import pytest
from selenium import webdriver

from pages.loginPage import login_page, login_method
from properties import test_data
from utils.dom_hunter import save_html_to_file


@pytest.mark.domHunt
class TestLogin:

    @pytest.fixture
    def driver(self):
        driver = webdriver.Chrome()
        yield driver
        driver.quit()

    # İstersen sadece belirli bir metoda da tag ekleyebilirsin
    @pytest.mark.regression
    def test_valid_login(self, driver):

        login_page(driver, test_data.login_url)  # Sayfayı açar ve maximize eder [1]
        login_method(driver, test_data.login_mail, test_data.instructor_password)

        def save_html_to_file(file_path):
            # Sayfanın HTML içeriğini al
            html_content = driver.page_source

            # HTML içeriğini dosyaya yaz
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(html_content)

        # HTML dosyasının yolu
        file_path = r"C:\Users\user\PycharmProjects\behaveFeature\reports\page_source2.html"

        # HTML içeriğini kaydet
        save_html_to_file(file_path)

        time.sleep(5)

        # Tarayıcıyı kapat
        driver.quit()


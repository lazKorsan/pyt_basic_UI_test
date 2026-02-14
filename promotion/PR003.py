import pytest
from selenium import webdriver
# Kaynaklardaki klasör yapına göre import [3, 4]
from pages.loginPage import login_page, login_method
from properties import test_data


# Tüm sınıfa "login" tag'i ekliyoruz
@pytest.mark.login
class TestLogin:

    @pytest.fixture
    def driver(self):
        driver = webdriver.Chrome()
        yield driver
        driver.quit()

    # İstersen sadece belirli bir metoda da tag ekleyebilirsin
    @pytest.mark.regression
    def test_valid_login(self, driver):
        """Geçerli bilgilerle login testi [1, 2]."""


        # Kaynaktaki fonksiyonları çağırıyoruz
        login_page(driver, test_data.login_url)  # Sayfayı açar ve maximize eder [1]
        login_method(driver, test_data.login_mail, test_data.instructor_password)  # Verileri girer ve tıklar [2]

        # Buraya doğrulama (assertion) eklenebilir
        assert "dashboard" in driver.current_url

    def test_invalid_login(self, driver):
        """Geçersiz bilgilerle login testi."""
        login_page(driver, test_data.login_url)
        login_method(driver, "yanlis@mail.com", "123")[2]

        # Hata mesajı kontrolü yapılabilir

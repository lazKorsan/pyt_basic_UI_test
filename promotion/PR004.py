import pytest
from selenium import webdriver
# Kaynaklardaki klasör yapısına göre import (pages/loginPage.py)
from pages.loginPage import login_page, login_method
from properties import test_data


# Java'daki DataProvider gibi çalışır
@pytest.mark.parametrize("mail, password", [
    (test_data.login_mail, test_data.instructor_password),
    ("lazKorsan@gmail.com", "Query.2026"),
    (test_data.login_mail, "Query.2025")
])
def test_multiple_logins(driver, mail, password):
    """Farklı veri setleri ile login testini koşturur."""



    # 1. Sayfayı açar ve maximize eder [1]
    login_page(driver, test_data.login_url)

    # 2. Parametreden gelen mail ve şifre ile giriş yapar [2]
    login_method(driver, mail, password)

    # 3. Doğrulama adımı (Örnek)
    # assert "error" not in driver.page_source

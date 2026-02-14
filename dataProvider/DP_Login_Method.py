import pytest
from selenium import webdriver
from pages.loginPage import login_page, login_method # Kaynağınızdaki metotlar [1, 2]
from properties import test_data


@pytest.fixture
def driver():
    # Tarayıcıyı burada başlatıyoruz
    driver = webdriver.Chrome()
    yield driver
    # Test bitince tarayıcıyı kapatıyoruz
    driver.quit()

@pytest.mark.parametrize("mail, password", [
    ("lazKorsan20260213072041@gmail.com", "Query.2026"),
    ("lazKorsan@gmail.com", "Query.2026"),
    ("lazKorsan20260213072041@gmail.com", "Query.2025")
])
def test_multiple_logins(driver, mail, password):

    login_page(driver, test_data.login_url) # Kaynaktaki sayfa açma metodu [1]
    login_method(driver, mail, password) # Kaynaktaki giriş metodu [2]

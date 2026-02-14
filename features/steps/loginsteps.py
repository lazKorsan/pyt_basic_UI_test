# loginsteps.py
from behave import given, when, then
from selenium import webdriver

from pages.loginPage import login_page, login_method # Kaynağınızdaki metotlar [1, 2]
from properties import test_data

@given('Kullanıcı giriş sayfasını açar')
def step_impl(context):
    # Kaynaktaki login_page metodunu çağırıyoruz [1]
    # Behave'de driver genellikle 'context' nesnesi üzerinden taşınır
    #context.driver = webdriver.Chrome()
    #context.driver.maximize_window()
    login_page(context.driver, test_data.login_url)

@when('Kullanıcı "{mail}" ve "{password}" bilgilerini girer')
def step_impl(context, mail, password):
    # Kaynaktaki login_method metodunu çağırıyoruz [2]
    # Parametreler feature dosyasındaki Examples tablosundan otomatik gelir
    login_method(context.driver, mail, password)

@then('Giriş işleminin gerçekleştiği doğrulanır')
def step_impl(context):
    # Burada girişin başarılı olduğunu doğrulamak için bir kontrol ekleyebilirsiniz
    # Örneğin URL değişimi kontrol edilebilir
    assert "dashboard" in context.driver.current_url

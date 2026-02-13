from behave import given, when, then
from selenium import webdriver

@given('Kullanıcı tarayıcıyı açar')
def step_impl(context):
    # Kaynaklarda bahsedilen WebDriver kullanımı burada gerçekleşir [1]
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()

@when('Kullanıcı "{url}" adresine gider')
def step_impl(context, url):
    context.driver.get(url)

@then('Sayfa başlığının "Google" içerdiğini doğrular')
def step_impl(context):
    assert "Google" in context.driver.title
    # Test bittikten sonra tarayıcıyı kapatmak iyi bir pratiktir
    context.driver.quit()
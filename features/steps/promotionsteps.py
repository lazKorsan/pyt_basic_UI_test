from behave import given, when

from pages import promotionPage
from pages.loginPage import login_method

from properties import test_data

@when(u'instuLearn kullanıcısı admin giriş yapar')
def step_impl(context):
    login_method(context.driver, test_data.login_mail, test_data.instructor_password)

@when(u'instulearn kullanıcısı promotion oluşturur')
def step_impl(context):
    promotionPage.promotion_pay(context.driver)

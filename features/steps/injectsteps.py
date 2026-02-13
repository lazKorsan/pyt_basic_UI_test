from behave import *
from selenium import webdriver
import time

from pages import registerPage
from properties.test_data import *
from utils.click_utils import click_utils

@given(u'Kullanici  "instuLearn" sayfasina gider')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get(register_URL)
    time.sleep(5)
@when(u'Kullanici instructor kullanici girisini secer')
def step_impl(context):
    click_utils(
        context.driver,
        registerPage.USERTYPESBUTTON_XPATH,
    )
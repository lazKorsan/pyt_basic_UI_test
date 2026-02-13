from behave import given, when, then
from selenium import webdriver

from pages.registerPage import register_method
from properties.test_data import instructor_name, instructor_password, register_URL


@given("user navigates to register page")
def step_navigate_register_page(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get(register_URL)


@when("user registers as instructor with valid name and password")
def step_register_instructor(context):
    context.email = register_method(
        context.driver,
        instructor_name,
        instructor_password
    )


@then("registration should be completed successfully")
def step_verify_register(context):
    # Şimdilik basit doğrulama (URL veya mail log)
    print(f"✅ Register başarılı -> {context.email}")
    assert context.email is not None

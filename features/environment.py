from selenium import webdriver

def before_scenario(context, scenario):
    # Her senaryodan önce tarayıcıyı başlatır ve context'e atar
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()

def after_scenario(context, scenario):
    # Senaryo bittiğinde tarayıcıyı kapatır
    if hasattr(context, "driver"):
        context.driver.quit()

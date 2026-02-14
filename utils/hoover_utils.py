from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HoverUtils:
    def __init__(self, driver):
        self.driver = driver

    def hover_and_style(self, xpath, element_color, center_color):
        # Elementi bul
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )

        # Hover işlemi
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

        # Elementin rengini değiştirme
        self.driver.execute_script(f"arguments[0].style.backgroundColor = '{element_color}';", element)

        # Merkezde renkli nokta ekleme
        self.driver.execute_script(f"""
            var dot = document.createElement('div');
            dot.style.width = '10px';
            dot.style.height = '10px';
            dot.style.backgroundColor = '{center_color}';
            dot.style.borderRadius = '50%';
            dot.style.position = 'absolute';
            dot.style.top = (arguments[0].offsetTop + arguments[0].offsetHeight / 2 - 5) + 'px';
            dot.style.left = (arguments[0].offsetLeft + arguments[0].offsetWidth / 2 - 5) + 'px';
            document.body.appendChild(dot);
        """, element)

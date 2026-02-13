from selenium import webdriver
import time

# WebDriver'ı başlat
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://qa.instulearn.com/register")

time.sleep(5)  # Sayfanın yüklenmesini beklemek için

def save_html_to_file(file_path):
    # Sayfanın HTML içeriğini al
    html_content = driver.page_source

    # HTML içeriğini dosyaya yaz
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(html_content)

# HTML dosyasının yolu
file_path = r"C:\Users\user\PycharmProjects\behaveFeature\reports\page_source.html"

# HTML içeriğini kaydet
save_html_to_file(file_path)

# Tarayıcıyı kapat
driver.quit()

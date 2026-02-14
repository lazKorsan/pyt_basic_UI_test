# dom_hunter.py
from selenium import webdriver
import time

# DEĞİŞİKLİK 1: Fonksiyon artık 'driver' nesnesini dışarıdan alıyor
def save_html_to_file(driver, file_path):
    """Aktif tarayıcıdaki sayfanın HTML içeriğini dosyaya yazar."""
    html_content = driver.page_source
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(html_content)

# DEĞİŞİKLİK 2: if __name__ == "__main__": bloğu
# Bu blok, dosya başka bir yerden import edildiğinde ÇALIŞMAZ.
# Sadece bu dosyayı sağ tıklayıp Run derseniz çalışır.
if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://qa.instulearn.com/register")
    time.sleep(5)

    file_path = r"C:\Users\user\PycharmProjects\behaveFeature\reports\page_source.html"
    save_html_to_file(driver, file_path)
    driver.quit()

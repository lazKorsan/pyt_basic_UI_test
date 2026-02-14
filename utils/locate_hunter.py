from bs4 import BeautifulSoup
import os
from lxml import etree
import re


def analyze_element_locators(html_file_path, output_file_path):
    """
    HTML dosyasındaki buton ve input elementlerinin locate'lerini analiz eder
    ve güçlüden zayıfa doğru sıralayarak çıktı dosyasına yazar.
    """

    # HTML dosyasını oku
    if not os.path.exists(html_file_path):
        print(f"Hata: {html_file_path} dosyası bulunamadı!")
        return

    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # BeautifulSoup ile parse et
    soup = BeautifulSoup(html_content, 'html.parser')

    # Elementleri bul
    elements = []

    # Butonları bul (button elementi ve type="button" olan inputlar)
    buttons = soup.find_all(['button', 'input'])
    for button in buttons:
        if button.name == 'button' or (button.name == 'input' and button.get('type') in ['button', 'submit', None]):
            elements.append(button)

    # Yazma kutularını bul (input text, textarea, input email, input password vb.)
    input_fields = []

    # Text input'lar
    text_inputs = soup.find_all('input', type=['text', 'email', 'password', 'search', 'tel', 'url', None])
    for inp in text_inputs:
        if inp.get('type') in ['text', 'email', 'password', 'search', 'tel', 'url', None] and inp.get(
                'type') != 'hidden':
            input_fields.append(inp)

    # Textarea'lar
    textareas = soup.find_all('textarea')
    input_fields.extend(textareas)

    elements.extend(input_fields)

    # Tekrarlanan elementleri kaldır
    elements = list(set(elements))

    # Elementleri analiz et ve locate'leri topla
    element_locations = []

    for element in elements:
        locators = []

        # ID (en güçlü)
        if element.get('id'):
            locators.append(('id', f"id={element['id']}", 10))

        # Name (güçlü)
        if element.get('name'):
            locators.append(('name', f"name={element['name']}", 9))

        # CSS Selector (orta-güçlü)
        css_selector = generate_css_selector(element)
        if css_selector:
            locators.append(('css', f"css={css_selector}", 8))

        # XPath (orta)
        xpath = generate_xpath(element)
        if xpath:
            locators.append(('xpath', f"xpath={xpath}", 7))

        # Class kombinasyonları (orta-zayıf)
        if element.get('class'):
            class_selector = generate_class_selector(element)
            if class_selector:
                locators.append(('class', f"class={class_selector}", 6))

        # Tag + text (butonlar için zayıf ama bazen işe yarar)
        if element.name == 'button' and element.get_text(strip=True):
            text = element.get_text(strip=True)[:30]  # Uzun text'leri kısalt
            locators.append(('text', f"text={text}", 5))

        # Tag + attribute (zayıf)
        if element.get('placeholder'):
            locators.append(('placeholder', f"placeholder={element['placeholder']}", 4))
        elif element.get('aria-label'):
            locators.append(('aria-label', f"aria-label={element['aria-label']}", 4))
        elif element.get('title'):
            locators.append(('title', f"title={element['title']}", 4))

        # Tag (en zayıf - sadece element tipi)
        locators.append(('tag', f"tag={element.name}", 3))

        # Locate'leri güç puanına göre sırala
        locators.sort(key=lambda x: x[2], reverse=True)

        # Element tipini belirle
        element_type = 'BUTTON' if element.name == 'button' or (
                    element.name == 'input' and element.get('type') in ['button', 'submit']) else 'INPUT'

        # Element hakkında bilgi topla
        element_info = {
            'type': element_type,
            'tag': element.name,
            'attributes': dict(element.attrs),
            'text': element.get_text(strip=True)[:50] if element.get_text(strip=True) else '',
            'locators': locators
        }

        element_locations.append(element_info)

    # Sonuçları dosyaya yaz
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write("=" * 80 + "\n")
        output_file.write("ELEMENT LOCATE ANALİZ RAPORU\n")
        output_file.write(f"Toplam Element Sayısı: {len(element_locations)}\n")
        output_file.write("=" * 80 + "\n\n")

        for i, elem in enumerate(element_locations, 1):
            output_file.write(f"[{i}] {elem['type']} ELEMENTİ\n")
            output_file.write("-" * 40 + "\n")
            output_file.write(f"Tag: {elem['tag']}\n")

            if elem['text']:
                output_file.write(f"Text: {elem['text']}\n")

            output_file.write("\nÖnemli Attribute'lar:\n")
            important_attrs = ['id', 'name', 'class', 'type', 'placeholder', 'aria-label', 'title', 'value']
            for attr in important_attrs:
                if attr in elem['attributes']:
                    output_file.write(f"  {attr}: {elem['attributes'][attr]}\n")

            output_file.write("\nLocate'ler (Güçlüden Zayıfa):\n")
            for loc_type, loc_value, score in elem['locators']:
                strength = "🔴 GÜÇLÜ" if score >= 9 else "🟠 ORTA" if score >= 7 else "🟡 ZAYIF"
                output_file.write(f"  {strength} - {loc_value}\n")

            output_file.write("\n" + "=" * 80 + "\n\n")

    print(f"Analiz tamamlandı! Sonuçlar {output_file_path} dosyasına kaydedildi.")
    print(f"Toplam {len(element_locations)} element bulundu.")


def generate_css_selector(element):
    """Element için CSS selector oluşturur"""
    selectors = []

    # ID varsa
    if element.get('id'):
        return f"#{element['id']}"

    # Class varsa
    if element.get('class'):
        classes = '.'.join(element['class'])
        selectors.append(f"{element.name}.{classes}")

    # Name varsa
    if element.get('name'):
        selectors.append(f"{element.name}[name='{element['name']}']")

    # Type varsa
    if element.get('type'):
        selectors.append(f"{element.name}[type='{element['type']}']")

    # Placeholder varsa
    if element.get('placeholder'):
        selectors.append(f"{element.name}[placeholder='{element['placeholder']}']")

    return selectors[0] if selectors else None


def generate_xpath(element):
    """Element için basit bir XPath oluşturur"""
    xpath_parts = []

    # Elementin kendisi
    xpath_parts.append(f"//{element.name}")

    # ID varsa
    if element.get('id'):
        return f"//{element.name}[@id='{element['id']}']"

    # Class varsa
    if element.get('class'):
        xpath_parts.append(f"[contains(@class, '{element['class'][0]}')]")

    # Name varsa
    if element.get('name'):
        xpath_parts.append(f"[@name='{element['name']}']")

    # Type varsa
    if element.get('type'):
        xpath_parts.append(f"[@type='{element['type']}']")

    # Placeholder varsa
    if element.get('placeholder'):
        xpath_parts.append(f"[@placeholder='{element['placeholder']}']")

    return ''.join(xpath_parts) if len(xpath_parts) > 1 else f"//{element.name}"


def generate_class_selector(element):
    """Element için class bazlı selector oluşturur"""
    if element.get('class'):
        classes = '.'.join(element['class'])
        return f"{element.name}.{classes}"
    return None


# Kullanım
if __name__ == "__main__":
    html_file = r"C:\Users\user\PycharmProjects\behaveFeature\reports\page_source2.html"
    output_file = r"C:\Users\user\PycharmProjects\behaveFeature\reports\element_locate_list.txt"

    analyze_element_locators(html_file, output_file)
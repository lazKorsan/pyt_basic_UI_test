from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import random

def highlight(driver, element, color="yellow", duration=0.5):
    """Elementi vurgula"""
    original_style = element.get_attribute('style')
    driver.execute_script(
        f"arguments[0].setAttribute('style', arguments[1]);", 
        element, 
        f"border: 3px solid {color}; background: #ffff99;"
    )
    time.sleep(duration)
    driver.execute_script(
        f"arguments[0].setAttribute('style', arguments[1]);", 
        element, 
        original_style
    )

def sendKey_utils(driver, locator, text, clear_first=True, press_enter=False, 
                  human_like=False, delay=0.1, highlight_color="yellow", timeout=10):
    """
    GELİŞMİŞ YAZMA FONKSİYONU - Her türlü senaryo için
    
    Args:
        driver: WebDriver instance
        locator: Element bulucu (XPATH string veya (By, value) tuple)
        text: Yazılacak metin
        clear_first: Önce temizleme (default: True)
        press_enter: Enter tuşuna bas (default: False)
        human_like: İnsan gibi yavaş yaz (default: False)
        delay: Karakter arası gecikme (default: 0.1sn)
        highlight_color: Vurgu rengi (default: "yellow")
        timeout: Bekleme süresi (default: 10sn)
    
    Returns:
        bool: İşlem başarılı mı?
    """
    
    print(f"\n{'='*70}")
    print(f"[sendKey_utils] 🚀 Yazma işlemi başlıyor...")
    print(f"[sendKey_utils]    ├─ Metin: '{text}'")
    print(f"[sendKey_utils]    ├─ Locator: {locator}")
    print(f"[sendKey_utils]    ├─ İnsan gibi: {human_like}")
    print(f"[sendKey_utils]    └─ Enter: {press_enter}")
    print(f"{'='*70}")
    
    # Locator tipini belirle
    if isinstance(locator, str):
        by_type = By.XPATH
        locator_value = locator
    else:
        by_type, locator_value = locator
    
    try:
        # 1. Elementi bul
        wait = WebDriverWait(driver, timeout)
        element = wait.until(EC.presence_of_element_located((by_type, locator_value)))
        
        # Element bilgilerini al
        tag = element.tag_name
        element_type = element.get_attribute('type')
        is_displayed = element.is_displayed()
        is_enabled = element.is_enabled()
        current_value = element.get_attribute('value') or '[empty]'
        
        print(f"[sendKey_utils] 🔍 Element bilgileri:")
        print(f"[sendKey_utils]    ├─ Tag: <{tag}>")
        print(f"[sendKey_utils]    ├─ Type: {element_type}")
        print(f"[sendKey_utils]    ├─ Görünür: {is_displayed}")
        print(f"[sendKey_utils]    ├─ Etkin: {is_enabled}")
        print(f"[sendKey_utils]    └─ Mevcut değer: '{current_value[:50]}...'")
        
        # Elementi vurgula
        highlight(driver, element, highlight_color)
        
        # ============= YAZMA YÖNTEMLERİ =============
        
        # YÖNTEM 1: Normal send_keys
        try:
            if clear_first:
                element.clear()
                time.sleep(0.2)
            
            if human_like:
                # İnsan gibi yazma
                for char in text:
                    element.send_keys(char)
                    time.sleep(random.uniform(0.05, 0.15))
            else:
                element.send_keys(text)
            
            if press_enter:
                element.send_keys(Keys.RETURN)
                print(f"[sendKey_utils] ✅ Enter tuşuna basıldı")
            
            print(f"[sendKey_utils] ✅ Yöntem 1 (Normal send_keys) BAŞARILI")
            return True
            
        except ElementNotInteractableException:
            print(f"[sendKey_utils] ⚠ Yöntem 1 başarısız - Element etkileşime kapalı")
        except Exception as e:
            print(f"[sendKey_utils] ⚠ Yöntem 1 başarısız - {str(e)[:50]}...")
        
        # YÖNTEM 2: JavaScript ile yazma
        try:
            if clear_first:
                driver.execute_script("arguments[0].value = '';", element)
            
            driver.execute_script(f"arguments[0].value = '{text}';", element)
            
            # Input event'ini tetikle
            driver.execute_script("""
                var event = new Event('input', { bubbles: true });
                arguments[0].dispatchEvent(event);
            """, element)
            
            if press_enter:
                driver.execute_script("""
                    var event = new KeyboardEvent('keydown', {
                        key: 'Enter',
                        code: 'Enter',
                        keyCode: 13,
                        which: 13,
                        bubbles: true
                    });
                    arguments[0].dispatchEvent(event);
                """, element)
            
            print(f"[sendKey_utils] ✅ Yöntem 2 (JavaScript) BAŞARILI")
            return True
        except Exception as e:
            print(f"[sendKey_utils] ⚠ Yöntem 2 başarısız - {str(e)[:50]}...")
        
        # YÖNTEM 3: ActionChains ile
        try:
            actions = ActionChains(driver)
            actions.move_to_element(element).click()
            
            if clear_first:
                actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL)
                actions.send_keys(Keys.DELETE)
            
            actions.send_keys(text)
            
            if press_enter:
                actions.send_keys(Keys.RETURN)
            
            actions.perform()
            print(f"[sendKey_utils] ✅ Yöntem 3 (ActionChains) BAŞARILI")
            return True
        except Exception as e:
            print(f"[sendKey_utils] ⚠ Yöntem 3 başarısız - {str(e)[:50]}...")
        
        # YÖNTEM 4: disabled kaldır + yaz
        try:
            driver.execute_script("arguments[0].disabled = false;", element)
            driver.execute_script("arguments[0].removeAttribute('readonly');", element)
            time.sleep(0.2)
            
            if clear_first:
                element.clear()
            element.send_keys(text)
            
            print(f"[sendKey_utils] ✅ Yöntem 4 (Disabled kaldır) BAŞARILI")
            return True
        except:
            pass
        
        # YÖNTEM 5: Clipboard ile yapıştır
        try:
            import pyperclip
            pyperclip.copy(text)
            
            element.click()
            
            if clear_first:
                driver.execute_script("arguments[0].select();", element)
                element.send_keys(Keys.DELETE)
            
            # Ctrl+V yapıştır
            actions = ActionChains(driver)
            actions.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL)
            actions.perform()
            
            print(f"[sendKey_utils] ✅ Yöntem 5 (Clipboard) BAŞARILI")
            return True
        except:
            print(f"[sendKey_utils] ⚠ Yöntem 5 için pyperclip gerekli")
        
        print(f"[sendKey_utils] ❌ TÜM YÖNTEMLER BAŞARISIZ!")
        return False
        
    except TimeoutException:
        print(f"[sendKey_utils] ❌ Element bulunamadı: {locator}")
        
        # Alternatif locator'ları dene
        alt_locators = []
        
        if isinstance(locator, str):
            alt_locators = [
                locator,
                f"{locator}[1]",
                locator.replace("input", "div"),
                locator.replace("@type='text'", ""),
                f"//*[@placeholder='{locator.split('@')[-1] if '@' in locator else ''}']"
            ]
            
            for i, alt_loc in enumerate(alt_locators[:3], 1):
                try:
                    print(f"[sendKey_utils] 🔄 Alternatif {i} deneniyor: {alt_loc}")
                    element = WebDriverWait(driver, 3).until(
                        EC.presence_of_element_located((By.XPATH, alt_loc))
                    )
                    highlight(driver, element, "orange")
                    element.send_keys(text)
                    print(f"[sendKey_utils] ✅ Alternatif {i} BAŞARILI!")
                    return True
                except:
                    continue
        
        return False

# ============= ÖZEL KULLANIM FONKSİYONLARI =============

def sendKey_utils_by_id(driver, element_id, text, **kwargs):
    """ID ile elemente yaz"""
    return sendKey_utils(driver, (By.ID, element_id), text, **kwargs)

def sendKey_utils_by_name(driver, name, text, **kwargs):
    """Name attribute ile elemente yaz"""
    return sendKey_utils(driver, (By.NAME, name), text, **kwargs)

def sendKey_utils_by_class(driver, class_name, text, **kwargs):
    """Class ile elemente yaz"""
    return sendKey_utils(driver, (By.CLASS_NAME, class_name), text, **kwargs)

def sendKey_utils_by_css(driver, css_selector, text, **kwargs):
    """CSS Selector ile elemente yaz"""
    return sendKey_utils(driver, (By.CSS_SELECTOR, css_selector), text, **kwargs)

def sendKey_utils_by_placeholder(driver, placeholder_text, text, **kwargs):
    """Placeholder attribute ile elemente yaz"""
    return sendKey_utils(
        driver, 
        (By.XPATH, f"//input[@placeholder='{placeholder_text}']"), 
        text, 
        **kwargs
    )

def sendKey_utils_by_label(driver, label_text, text, **kwargs):
    """Label metnine göre input bul ve yaz"""
    xpath = f"//label[contains(text(), '{label_text}')]/following::input[1]"
    return sendKey_utils(driver, xpath, text, **kwargs)

def sendKey_utils_random_text(driver, locator, length=10, **kwargs):
    """Rastgele metin oluştur ve yaz"""
    import random
    import string
    
    random_text = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    print(f"[sendKey_utils] 🎲 Rastgele metin: '{random_text}'")
    return sendKey_utils(driver, locator, random_text, **kwargs)

def sendKey_utils_password(driver, locator, **kwargs):
    """Güçlü şifre oluştur ve yaz"""
    import random
    import string
    
    password = ''.join([
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice("!@#$%"),
        ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    ])
    print(f"[sendKey_utils] 🔐 Şifre oluşturuldu: {'*' * len(password)}")
    return sendKey_utils(driver, locator, password, **kwargs)

def sendKey_utils_email(driver, locator, prefix="test", **kwargs):
    """Rastgele email oluştur ve yaz"""
    import random
    import string
    
    domains = ["example.com", "test.com", "demo.com", "instulearn.com"]
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    email = f"{prefix}.{random_string}@{random.choice(domains)}"
    
    print(f"[sendKey_utils] 📧 Email oluşturuldu: {email}")
    return sendKey_utils(driver, locator, email, **kwargs)

def sendKey_utils_phone(driver, locator, **kwargs):
    """Rastgele telefon numarası oluştur ve yaz"""
    import random
    
    phone = f"5{random.randint(10, 99)}{random.randint(100, 999)}{random.randint(1000, 9999)}"
    print(f"[sendKey_utils] 📱 Telefon: {phone}")
    return sendKey_utils(driver, locator, phone, **kwargs)

def sendKey_utils_date(driver, locator, days_offset=0, **kwargs):
    """Bugünün tarihini veya offset'li tarihi yaz"""
    from datetime import datetime, timedelta
    
    date = datetime.now() + timedelta(days=days_offset)
    date_str = date.strftime("%d.%m.%Y")
    
    print(f"[sendKey_utils] 📅 Tarih: {date_str}")
    return sendKey_utils(driver, locator, date_str, **kwargs)

def sendKey_utils_clear(driver, locator, **kwargs):
    """Elementi temizle"""
    return sendKey_utils(driver, locator, "", clear_first=True, **kwargs)

def sendKey_utils_append(driver, locator, text, **kwargs):
    """Mevcut değerin sonuna ekle"""
    return sendKey_utils(driver, locator, text, clear_first=False, **kwargs)
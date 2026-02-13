from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
import time

def highlight(driver, element, color="yellow", duration=1):
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

def click_utils(driver, xpath, color="yellow", timeout=10):
    """
    İnatçı butonlar için gelişmiş tıklama fonksiyonu
    
    Args:
        driver: WebDriver instance
        xpath: Butonun XPATH'i
        color: Vurgu rengi (default: yellow)
        timeout: Bekleme süresi (default: 10)
    
    Returns:
        bool: Tıklama başarılı mı?
    """
    print(f"\n{'='*60}")
    print(f"[click_utils] 🚀 Buton tıklama denemesi başlıyor...")
    print(f"[click_utils]    ├─ XPATH: {xpath}")
    print(f"[click_utils]    ├─ Renk: {color}")
    print(f"[click_utils]    └─ Timeout: {timeout}sn")
    print(f"{'='*60}")
    
    try:
        # 1. Elementi bul ve tıklanabilir olana kadar bekle
        wait = WebDriverWait(driver, timeout)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        
        # Element bilgilerini al
        visible = element.is_displayed()
        enabled = element.is_enabled()
        text = element.text.strip() or element.get_attribute('value') or element.get_attribute('innerText') or 'NoText'
        tag = element.tag_name
        
        print(f"[click_utils] 🔍 Buton bilgileri:")
        print(f"[click_utils]    ├─ Tag: <{tag}>")
        print(f"[click_utils]    ├─ Text: '{text}'")
        print(f"[click_utils]    ├─ Görünür: {visible}")
        print(f"[click_utils]    └─ Tıklanabilir: {enabled}")
        
        # Elementi vurgula
        highlight(driver, element, color)
        
        # ============= TIKLAMA YÖNTEMLERİ =============
        
        # YÖNTEM 1: Normal click
        try:
            element.click()
            print(f"[click_utils] ✅ Yöntem 1 (Normal click) BAŞARILI: '{text}'")
            return True
            
        except ElementClickInterceptedException:
            print(f"[click_utils] ⚠ Yöntem 1 başarısız - Element başka element tarafından engelleniyor")
        except Exception as e:
            print(f"[click_utils] ⚠ Yöntem 1 başarısız - {str(e)[:50]}...")
        
        # YÖNTEM 2: JavaScript click
        try:
            driver.execute_script("arguments[0].click();", element)
            print(f"[click_utils] ✅ Yöntem 2 (JavaScript click) BAŞARILI: '{text}'")
            return True
        except Exception as e:
            print(f"[click_utils] ⚠ Yöntem 2 başarısız - {str(e)[:50]}...")
        
        # YÖNTEM 3: ActionChains
        try:
            actions = ActionChains(driver)
            actions.move_to_element(element).click().perform()
            print(f"[click_utils] ✅ Yöntem 3 (ActionChains) BAŞARILI: '{text}'")
            return True
        except Exception as e:
            print(f"[click_utils] ⚠ Yöntem 3 başarısız - {str(e)[:50]}...")
        
        # YÖNTEM 4: Scroll + click
        try:
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
            time.sleep(0.5)
            element.click()
            print(f"[click_utils] ✅ Yöntem 4 (Scroll + click) BAŞARILI: '{text}'")
            return True
        except Exception as e:
            print(f"[click_utils] ⚠ Yöntem 4 başarısız - {str(e)[:50]}...")
        
        # YÖNTEM 5: Submit (eğer form elementi ise)
        if tag == 'button' or tag == 'input':
            try:
                element.submit()
                print(f"[click_utils] ✅ Yöntem 5 (Submit) BAŞARILI: '{text}'")
                return True
            except:
                pass
        
        # YÖNTEM 6: Parent click
        try:
            parent = driver.execute_script("return arguments[0].parentNode;", element)
            if parent:
                driver.execute_script("arguments[0].click();", parent)
                print(f"[click_utils] ✅ Yöntem 6 (Parent click) BAŞARILI: '{text}'")
                return True
        except:
            pass
        
        # YÖNTEM 7: disabled kaldır + click
        try:
            driver.execute_script("arguments[0].disabled = false;", element)
            time.sleep(0.2)
            element.click()
            print(f"[click_utils] ✅ Yöntem 7 (Disabled kaldır + click) BAŞARILI: '{text}'")
            return True
        except:
            pass
        
        # YÖNTEM 8: readonly kaldır + click
        try:
            driver.execute_script("arguments[0].removeAttribute('readonly');", element)
            time.sleep(0.2)
            element.click()
            print(f"[click_utils] ✅ Yöntem 8 (Readonly kaldır + click) BAŞARILI: '{text}'")
            return True
        except:
            pass
        
        # YÖNTEM 9: Mouse event
        try:
            driver.execute_script("""
                var event = new MouseEvent('click', {
                    view: window,
                    bubbles: true,
                    cancelable: true
                });
                arguments[0].dispatchEvent(event);
            """, element)
            print(f"[click_utils] ✅ Yöntem 9 (Mouse Event) BAŞARILI: '{text}'")
            return True
        except:
            pass
        
        print(f"[click_utils] ❌ TÜM YÖNTEMLER BAŞARISIZ! Butona tıklanamadı: '{text}'")
        return False
        
    except TimeoutException:
        print(f"[click_utils] ❌ Buton bulunamadı veya tıklanabilir değil: {xpath}")
        
        # Alternatif XPATH'leri dene
        # Extract text from xpath if it contains quoted text
        extracted_text = ""
        if "'" in xpath:
            try:
                extracted_text = xpath.split("'")[1]
            except IndexError:
                extracted_text = ""
        
        alt_xpaths = [
            xpath,
            f"{xpath}[1]",
            f"({xpath})[1]",
            xpath.replace("button", "div"),
            xpath.replace("@type='submit'", "@type='button'"),
            xpath.replace("contains(text(),", "contains(@value,"),
            f"//*[contains(text(), '{extracted_text}')]" if extracted_text else xpath,
        ]
        
        for i, alt_xpath in enumerate(alt_xpaths[:3], 1):  # İlk 3 alternatifi dene
            try:
                print(f"[click_utils] 🔄 Alternatif {i} deneniyor: {alt_xpath}")
                element = WebDriverWait(driver, 3).until(
                    EC.element_to_be_clickable((By.XPATH, alt_xpath))
                )
                highlight(driver, element, "orange", 0.5)
                element.click()
                print(f"[click_utils] ✅ Alternatif {i} BAŞARILI!")
                return True
            except:
                continue
        
        return False
    
    except Exception as e:
        print(f"[click_utils] ❌ Beklenmeyen hata: {str(e)}")
        return False

def click_utils_by_text(driver, text, tag="button", color="purple", timeout=10):
    """Buton metnine göre tıkla"""
    xpath = f"//{tag}[contains(text(), '{text}')]"
    print(f"[click_utils] 🔍 Metin ile buton aranıyor: '{text}'")
    return click_utils(driver, xpath, color, timeout)

def click_utils_by_css(driver, css_selector, color="blue", timeout=10):
    """CSS Selector ile tıkla"""
    from selenium.webdriver.common.by import By
    print(f"[click_utils] 🔍 CSS Selector ile buton aranıyor: {css_selector}")
    
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector))
        )
        highlight(driver, element, color, 0.5)
        element.click()
        print(f"[click_utils] ✅ CSS Selector tıklama başarılı!")
        return True
    except:
        return click_utils(driver, f"//*[@id='{css_selector}']", color, timeout)


########################################################

def click_checkbox_utils(driver, xpath=None, element=None, color="green", timeout=10):
    """
    İNATÇI CHECKBOX'LAR İÇİN ÖZEL FONKSİYON!
    Label'a, span'e, div'e, parent'a tüm yöntemleri dener.
    """
    print(f"\n{'='*70}")
    print(f"[click_checkbox_utils] 🎯 Checkbox tıklama başlıyor...")
    print(f"{'='*70}")
    
    # Element verilmemişse XPATH'den bul
    if element is None and xpath:
        try:
            wait = WebDriverWait(driver, timeout)
            element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        except:
            print(f"[click_checkbox_utils] ❌ Checkbox bulunamadı: {xpath}")
            return False
    
    if not element:
        return False
    
    # ============= TÜM TIKLAMA YÖNTEMLERİ =============
    
    methods = [
        # 1. Direkt checkbox'a tıkla
        lambda: element.click(),
        
        # 2. JavaScript ile checkbox'a tıkla
        lambda: driver.execute_script("arguments[0].click();", element),
        
        # 3. Label'a tıkla (for attribute)
        lambda: driver.find_element(By.XPATH, f"//label[@for='{element.get_attribute('id')}']").click(),
        
        # 4. Parent div'e tıkla
        lambda: driver.execute_script("arguments[0].parentNode.click();", element),
        
        # 5. Parent'ın parent'ına tıkla
        lambda: driver.execute_script("arguments[0].parentNode.parentNode.click();", element),
        
        # 6. Following-sibling (span veya div)
        lambda: driver.execute_script("arguments[0].nextSibling.click();", element),
        
        # 7. Custom-control sınıfına tıkla
        lambda: driver.find_element(By.XPATH, f"//div[contains(@class, 'custom-control') and .//input[@id='{element.get_attribute('id')}']]").click(),
        
        # 8. ActionChains ile tıkla
        lambda: ActionChains(driver).move_to_element(element).click().perform(),
        
        # 9. ActionChains ile label'a tıkla
        lambda: ActionChains(driver).move_to_element(driver.find_element(By.XPATH, f"//label[@for='{element.get_attribute('id')}']")).click().perform(),
        
        # 10. Space tuşu ile
        lambda: element.send_keys(Keys.SPACE),
        
        # 11. Enter tuşu ile
        lambda: element.send_keys(Keys.RETURN),
        
        # 12. Checkbox'ı manuel set et (JS)
        lambda: driver.execute_script("arguments[0].checked = true; arguments[0].dispatchEvent(new Event('change', {bubbles: true}));", element),
        
        # 13. CSS ile background'a tıkla
        lambda: driver.execute_script("""
            var checkbox = arguments[0];
            var rect = checkbox.getBoundingClientRect();
            var event = new MouseEvent('click', {
                view: window,
                bubbles: true,
                cancelable: true,
                clientX: rect.left + rect.width/2,
                clientY: rect.top + rect.height/2
            });
            checkbox.dispatchEvent(event);
        """, element),
        
        # 14. Tüm sibling'leri dene
        lambda: driver.execute_script("""
            var el = arguments[0];
            var parent = el.parentNode;
            while(parent) {
                if(parent.click) { parent.click(); break; }
                parent = parent.parentNode;
            }
        """, element),
    ]
    
    # Tüm metodları dene
    for i, method in enumerate(methods, 1):
        try:
            # Elementi vurgula
            highlight(driver, element, color, 0.3)
            time.sleep(0.2)
            
            method()
            
            # Checkbox seçildi mi kontrol et
            is_checked = driver.execute_script("return arguments[0].checked;", element)
            
            if is_checked:
                print(f"[click_checkbox_utils] ✅ Yöntem {i} BAŞARILI! Checkbox seçildi.")
                
                # Başarılı yöntemi tekrar vurgula
                highlight(driver, element, "green", 0.5)
                return True
            else:
                print(f"[click_checkbox_utils] ⚠ Yöntem {i} çalıştı ama checkbox seçilmedi?")
                
        except Exception as e:
            print(f"[click_checkbox_utils] ⚠ Yöntem {i} başarısız: {str(e)[:30]}...")
            continue
    
    # SON ÇARE: Tüm sayfadaki checkbox'ları dene!
    try:
        print(f"[click_checkbox_utils] 🔄 SON ÇARE: Tüm checkbox'lar taranıyor...")
        all_checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
        
        for idx, cb in enumerate(all_checkboxes):
            try:
                driver.execute_script("arguments[0].checked = true; arguments[0].dispatchEvent(new Event('change'));", cb)
                print(f"[click_checkbox_utils] ✅ Son çare - Checkbox {idx+1} seçildi!")
                return True
            except:
                continue
    except:
        pass
    
    print(f"[click_checkbox_utils] ❌ TÜM YÖNTEMLER BAŞARISIZ!")
    return False


def click_terms_checkbox(driver, timeout=10):
    """Özel olarak terms&conditions checkbox'ını tıkla"""
    
    # Tüm olası XPATH'leri dene
    xpaths = [
        "//input[@type='checkbox' and @id='term']",
        "//input[@type='checkbox' and @name='term']",
        "//label[@for='term']",
        "//div[contains(@class, 'custom-checkbox')]",
        "//span[contains(@class, 'custom-control')]",
        "//label[contains(text(), 'I agree')]",
        "//label[contains(text(), 'terms')]/..",
        "(//input[@type='checkbox'])[1]",
        "(//input[@type='checkbox'])[last()]",
    ]
    
    for xpath in xpaths:
        try:
            element = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            
            # Eğer element label veya div ise, içindeki checkbox'ı bul
            if element.tag_name in ['label', 'div', 'span']:
                # İçinde input checkbox var mı?
                checkbox = element.find_elements(By.XPATH, ".//input[@type='checkbox']")
                if checkbox:
                    return click_checkbox_utils(driver, element=checkbox[0])
            
            # Direkt tıkla
            return click_checkbox_utils(driver, element=element)
            
        except:
            continue
    
    return False    
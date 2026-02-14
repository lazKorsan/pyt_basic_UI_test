import subprocess
import os
import sys

# Rapor klasörü kontrolü [1]
if not os.path.exists("reports"):
    os.makedirs("reports")

def run_behave_comprehensive(tag_name):
    print(f"--- {tag_name} Testleri Başlatılıyor (Rapor + Canlı Log) ---")

    # Komut Analizi:
    # --no-capture: Print çıktılarını terminalde gösterir.
    # --format & --outfile: Belirttiğiniz formatlarda raporları hazırlar.
    command = (
        f"behave --tags={tag_name} --no-capture --no-capture-stderr "
        "--format behave_html_formatter:HTMLFormatter --outfile reports/behave_report.html "
        "--format allure_behave.formatter:AllureFormatter --outfile reports/allure_results "
        "--format pretty" # Terminalde stepleri renkli ve güzel gösterir
    )

    try:
        subprocess.run(command, shell=True, check=True)
        print("\n[BAŞARILI] Testler bitti ve raporlar 'reports/' klasöründe güncellendi.")
    except subprocess.CalledProcessError:
        print("\n[HATA] Testler sırasında bir sorun oluştu veya eksik step var.")

if __name__ == "__main__":
    # Kaynaklardaki login metotlarınızı [2, 3] koşturmak için:
    run_behave_comprehensive("@promotion")


# allure serve reports/allure_results
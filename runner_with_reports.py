import subprocess
import os
import sys

# Rapor klasörü kontrolü (Kaynak 3'te görünen dizin yapısına uygun)
if not os.path.exists("reports"):
    os.makedirs("reports")

def run_smoke_with_reporting():
    print("--- @login Tag'li Testler Raporlu Olarak Başlatılıyor ---")

    # ÇÖZÜM: Her satırın başına veya sonuna boşluk ekleyerek komutları ayırıyoruz
    command = (
        "behave --tags=@login " # Buradaki boşluk kritik!
        "--format behave_html_formatter:HTMLFormatter --outfile reports/behave_report.html "
        "--format allure_behave.formatter:AllureFormatter --outfile reports/allure_results"
    )

    try:
        # Komutu çalıştır
        subprocess.run(command, shell=True, check=True)
        print("\n[BAŞARILI] Raporlar 'reports/' klasöründe oluşturuldu.")
    except subprocess.CalledProcessError as e:
        print(f"\n[HATA] Testler başarısız oldu veya yapılandırma hatası var: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_smoke_with_reporting()

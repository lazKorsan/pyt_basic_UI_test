import subprocess
import os
import sys

# Rapor klasörü kontrolü
if not os.path.exists("reports"):
    os.makedirs("reports")

def run_smoke_with_reporting():
    print("--- @dynamicRegister Tag'li Testler Başlatılıyor ---")

    # ÇÖZÜM: --format html yerine behave_html_formatter:HTMLFormatter kullanıyoruz
    command = (
        "behave --tags=@dynamicRegister "
        "--format behave_html_formatter:HTMLFormatter --outfile reports/behave_report.html "
        "--format allure_behave.formatter:AllureFormatter --outfile reports/allure_results"
    )

    try:
        subprocess.run(command, shell=True, check=True)
        print("\n[BAŞARILI] Raporlar 'reports/' klasöründe oluşturuldu.")
    except subprocess.CalledProcessError:
        print("\n[HATA] Testler başarısız oldu veya yapılandırma hatası var.")
        sys.exit(1)

if __name__ == "__main__":
    run_smoke_with_reporting()

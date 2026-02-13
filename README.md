1. Proje Klasör Yapısı (Hiyerarşi)
Kaynaklarda belirtilen ideal yapılanmaya uygun olarak dosyalarınız şu konumda olmalıdır:
Proje_Klasoru/
├── .venv/                  # Sanal ortam
├── features/               # Senaryo (Gherkin) dosyaları
│   ├── steps/              # Python kodları (Step Definitions)
│   │   └── google_steps.py
│   └── google_acma.feature
├── reports/                # Test raporlarının saklandığı yer
├── pytest.ini              # Merkezi konfigürasyon dosyası
├── requirements.txt        # Gerekli kütüphaneler listesi
├── runner.py               # Test tetikleyici script
└── environment.py          # Hooks (Before/After) yapılandırması
2. Kurulum ve Bağımlılıklar (requirements.txt)
Projeyi ilk kez kurarken terminalden pip install -r requirements.txt komutunu çalıştırın. Dosya içeriği tam olarak şöyledir:
selenium==4.40.0
fixture==1.5.11
pytest==9.0.2
behave==1.3.3
requests==2.32.5
pandas==3.0.0
behave-html-formatter==0.9.10
allure-behave==2.15.3
Not: Bu sürümler sizin belirttiğiniz güncel çalışma ortamınıza aittir.
3. Merkezi Konfigürasyon (pytest.ini)
Projenin ana dizininde yer alan bu dosya, testlerin davranışını ve WebDriver parametrelerini yönetir:
[pytest]
addopts = -vs --browser chrome
testpaths = features
markers =
    smoke: Kritik test senaryoları
    regression: Tüm sistem testleri
4. Feature ve Steps Yapılandırması
İdeal bir yapılanmada iş mantığı (feature) ve uygulama kodu (steps) birbirinden ayrılır.
• Feature: features/google_acma.feature içinde @smoke tag'i ile tanımlanır.
• Steps: features/steps/google_steps.py içinde from behave import given, when, then import yapısı kullanılarak kodlanır.
5. Testleri Çalıştırma ve Runner Yapısı
Testleri en basit haliyle terminalden şu komutla koşturabilirsiniz: behave --tags=@smoke
Ancak raporlamayı da kapsayan Python Runner yapısı şöyledir:
import subprocess
# @smoke tag'li testleri koşturur ve rapor üretir
command = (
    "behave --tags=@smoke "
    "--format behave_html_formatter:HTMLFormatter --outfile reports/report.html "
    "--format allure_behave.formatter:AllureFormatter --outfile reports/allure_results"
)
subprocess.run(command, shell=True)
6. Raporlama (Allure Reports)
Test sonuçlarını profesyonel bir arayüzde görmek için şu adımları izleyin:
1. Veri Üretimi: Yukarıdaki runner veya terminal komutu ile reports/allure_results klasörüne verilerin yazıldığından emin olun.
2. Raporu Görüntüleme: Terminale şu komutu yazarak (Allure sisteminizde kuruluysa) görsel raporu açın: allure serve reports/allure_results
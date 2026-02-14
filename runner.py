# runner.py
import subprocess
import sys


# Kaynak dışı teknik bilgi: Behave testlerini Python üzerinden
# tag ile çalıştırmak için subprocess veya behave kütüphanesi kullanılır.

def run_behave_tests(tag_name):
    print(f"--- {tag_name} etiketli testler başlatılıyor ---")

    # Komut satırı üzerinden behave'i çağıran komut
    # -t parametresi belirlenen tag'e sahip senaryoları seçer
    command = f"behave --tags={tag_name}"

    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Test koşturulurken hata oluştu: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # İlk tag olarak yukarıdaki testte kullandığımız @smoke tag'ini veriyoruz
    run_behave_tests("@promotion")

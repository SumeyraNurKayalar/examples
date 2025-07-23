from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import random

def trendyol_scrape(keyword):
    # Chrome ayarları
    options = Options()
    options.add_argument("--headless")  # Arka planda çalıştırmak için
    options.add_argument("--disable-gpu")
    options.add_argument("start-maximized")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")

    # Driver başlat
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        # Trendyol'da arama yap
        search_url = f"https://www.trendyol.com/sr?q={keyword}"
        driver.get(search_url)

        # Rastgele delay simülasyonu (bot gibi görünmemek için)
        time.sleep(random.uniform(2, 4))

        # Ürün kartlarını al
        products = driver.find_elements(By.CLASS_NAME, "p-card-chldrn-cntnr")

        results = []
        for product in products[:10]:  # İlk 10 ürünü al
            try:
                title = product.find_element(By.CLASS_NAME, "prdct-desc-cntnr").text
                price = product.find_element(By.CLASS_NAME, "prc-box-dscntd").text
                results.append((title, price))
            except:
                continue

        # Sonuçları yazdır
        print(f"\n Arama sonucu: {keyword}\n")
        for idx, (title, price) in enumerate(results, start=1):
            print(f"{idx}. {title} - {price}")

    finally:
        driver.quit()

if __name__ == "__main__":
    urun = input("Aramak istediğiniz ürün: ")
    trendyol_scrape(urun)

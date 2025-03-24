import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlparse

# Para FireFox
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def get_playlist_id(url):
    parsed_url = urlparse(url)
    playlist_id = parsed_url.path.split('/')[-1]
    return playlist_id

def scrape_spotify(url):
    # Configurar Selenium
    options = Options()
    options.add_argument('--headless')  # Ejecutar en modo headless
    options.add_argument('--no-sandbox')  # Requerido para algunos servidores
    options.add_argument('--disable-dev-shm-usage')  # Para evitar errores de memoria

    # Configurar el servicio de GeckoDriver
    service = Service("/usr/local/bin/geckodriver")
    # Crear el WebDriver de Firefox
    driver = webdriver.Firefox(service=service, options=options)

    # Navegar al sitio web
    driver.get(url)

    time.sleep(10)  # Esperar a que la página cargue

    print(driver.title)  # Para depuración
    # Esperar a que los elementos estén presentes
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h1"))
        )
        playlist_name = driver.find_element(By.CSS_SELECTOR, "h1").text

        # Desplazarse hacia abajo para cargar más elementos
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)  # Reduce el tiempo de espera para acelerar el proceso
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        
        # Esperar a que todos los elementos se carguen
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[data-testid='tracklist-row']"))
        )
        song_elements = driver.find_elements(By.CSS_SELECTOR, "div[data-testid='tracklist-row']")
    except Exception as e:
        print("Error al encontrar los elementos:", e)
        driver.quit()
        return []

    scraped_data = []
    for song in song_elements:
        song_name = song.find_element(By.CSS_SELECTOR, "div.e-9640-text.encore-text-body-medium.encore-internal-color-text-base.btE2c3IKaOXZ4VNAb8WQ.standalone-ellipsis-one-line").text
        artist_elements = song.find_elements(By.CSS_SELECTOR, "a[href*='/artist/']")
        artists = ", ".join([artist.text for artist in artist_elements])
        scraped_data.append({
            "playlist_name": playlist_name,
            "song_name": song_name,
            "artist": artists
        })

    print("Scraped data:", scraped_data)  # Para depuración
    driver.quit()
    return scraped_data

if __name__ == "__main__":
    url = ""
    web_data = scrape_spotify(url)

    print("Web Data:", web_data)
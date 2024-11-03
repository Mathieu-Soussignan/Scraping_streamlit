import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from src.utils import log_error
import time
from selenium.webdriver.chrome.service import Service

def run_scraping(url):
    # Configurer les options pour Chrome
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--headless')  # Facultatif : exécuter sans interface graphique

    # Créer une instance du WebDriver avec les options
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    # Accéder à la page de recherche
    driver.get(url)

    # Attendre que les résultats de recherche soient chargés
    try:
        results = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".s-result-item"))
        )
    except Exception as e:
        log_error(f"Erreur lors du chargement des résultats : {e}")
        driver.quit()
        return
    
    # Extraire les données
    titles = []
    prices = []
    
    for result in results[:10]:  # Limité à 10 produits
        try:
            # Utilisation d'un sélecteur alternatif pour le titre
            title_element = result.find_element(By.CSS_SELECTOR, "span.a-text-normal")
            title = title_element.text if title_element else "N/A"
            titles.append(title)
            print(f"Titre extrait : {title}")  # Débogage
            
            # Utilisation d'un sélecteur alternatif pour le prix
            try:
                price_element = result.find_element(By.CSS_SELECTOR, "span.a-price-whole")
                price = price_element.text if price_element else "N/A"
                prices.append(price)
                print(f"Prix extrait : {price}")  # Débogage
            except Exception as e:
                prices.append("N/A")
                log_error(f"Erreur d'extraction du prix : {e}")
            
        except Exception as e:
            titles.append("N/A")
            prices.append("N/A")
            log_error(f"Erreur d'extraction des données : {e}")

    # Sauvegarder les données dans un fichier CSV
    data = pd.DataFrame({
        "Title": titles,
        "Price": prices
    })
    data.to_csv("data/produits_amazon.csv", index=False)
    print("Les données ont été sauvegardées dans 'data/produits_amazon.csv'.")

    # Fermer le navigateur
    driver.quit()
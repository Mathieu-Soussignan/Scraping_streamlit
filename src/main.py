import sys
import os

# Ajoutez le chemin du dossier src au sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from src.scraping import run_scraping
from src.config import URL

def main():
    print("Début du scraping...")
    run_scraping(URL)
    print("Scraping terminé. Les données sont sauvegardées dans le dossier 'data'.")

if __name__ == "__main__":
    main()
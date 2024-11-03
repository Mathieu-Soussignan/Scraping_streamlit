# Scraping Amazon avec Streamlit

Ce projet est une application Streamlit qui permet de scraper les données de produits Amazon en fonction d'une catégorie choisie par l'utilisateur. L'application affiche les produits dans un tableau interactif, permet de filtrer les résultats par prix et marque, et d'exporter les données en fichier Excel.

## Fonctionnalités

- **Sélection de catégorie de produits** : Choisissez parmi plusieurs catégories (smartphone, ordinateur, tablette, etc.).
- **Filtrage par prix** : Définissez une limite de prix maximale pour les produits affichés.
- **Filtrage par marque** : Filtrez les produits par marque (si cette information est disponible).
- **Tri des résultats** : Triez les produits par prix ou par ordre alphabétique.
- **Affichage structuré des données** : Affichage des produits dans un tableau interactif et structuré.
- **Export en fichier Excel** : Téléchargez les résultats filtrés sous forme de fichier Excel.
- **Graphique de distribution des prix** : Visualisez la répartition des prix des produits avec un histogramme.

## Prérequis

- Python 3.7 ou version ultérieure
- `pip` pour gérer les packages Python

## Installation

1. Clonez le dépôt ou téléchargez le code source :

   ```bash
   git clone https://github.com/votre-utilisateur/nom-du-repo.git
   cd nom-du-repo
   ```

2. Créez un environnement virtuel et activez-le :

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Sur macOS et Linux
   .venv\Scripts\activate     # Sur Windows
   ```

3. Installez les dépendances nécessaires :

   ```bash
   pip install -r requirements.txt
   ```

4. Installez `chromedriver` : Assurez-vous d'avoir Chrome et `chromedriver` installés pour exécuter le scraping avec Selenium. Vous pouvez installer `chromedriver` via `webdriver-manager`, inclus dans les dépendances.

## Utilisation

1. Exécutez l'application Streamlit :

   ```bash
   streamlit run app.py
   ```

2. Une fois l’application lancée, ouvrez le navigateur à l’adresse indiquée (par défaut : `http://localhost:8501`).

3. **Sélection de la catégorie de produits** : Dans l'interface, sélectionnez la catégorie de produits souhaitée.

4. Cliquez sur le bouton **Lancer le Scraping** pour démarrer le scraping des produits de la catégorie choisie. Une barre de progression vous indiquera l'avancement du scraping.

5. **Filtrage et affichage** :

   - Utilisez le curseur pour définir une limite de prix maximale.
   - Filtrez les produits par marque si cette information est disponible.
   - Choisissez une option de tri pour organiser les produits affichés.

6. **Exportation et visualisation** :

   - Cliquez sur **Exporter en Excel** pour télécharger les résultats filtrés.
   - Un histogramme montre la répartition des prix des produits affichés.

## Détails des fichiers

- `.streamlit/config.toml` : Fichier de configuration pour l'application Streamlit.
- `app.py` : Le script principal de l'application Streamlit.
- `src/scraping.py` : Contient la fonction `run_scraping()` qui utilise Selenium pour récupérer les données des produits sur Amazon.
- `data/produits_amazon.csv` : Fichier CSV généré après le scraping, contenant les informations des produits récupérés.
- `requirements.txt` : Liste des dépendances nécessaires pour exécuter le projet.
- `assets/` : Dossier contenant les fichiers de ressources, tels que les images.

## Structure du Projet

```
nom-du-repo/
├── .streamlit/
│   └── config.toml
├── assets/                # Fichiers de ressources (images, etc.)
├── app.py                 # Application principale Streamlit
├── src/
│   └── scraping.py        # Fonction de scraping avec Selenium
├── data/
│   └── produits_amazon.csv # Fichier CSV des produits
├── requirements.txt       # Fichier de dépendances
└── README.md              # Documentation du projet
```

## Dépendances principales

- **Streamlit** : Pour l'interface utilisateur.
- **Selenium** : Pour le scraping des données d'Amazon.
- **pandas** : Pour la manipulation des données.
- **matplotlib** : Pour l'affichage du graphique de distribution des prix.
- **xlsxwriter** : Pour l'exportation des données en fichier Excel.

## Notes et Limitations

- **Légalité du scraping** : Veuillez noter que scraper des sites comme Amazon peut être soumis à leurs conditions d'utilisation. Assurez-vous d'avoir l'autorisation ou d'utiliser ce projet uniquement à des fins éducatives.
- **Limitations de vitesse** : Pour éviter d'être bloqué, évitez d'effectuer des scrapes intensifs ou répétitifs en peu de temps.
- **Dépendance de `chromedriver`** : Assurez-vous que `chromedriver` est compatible avec la version de Chrome installée sur votre machine.

## Exemple d'utilisation

1. Lancez l’application avec la commande `streamlit run app.py`.
2. Sélectionnez une catégorie de produit, par exemple "smartphone".
3. Cliquez sur **Lancer le Scraping**.
4. Une fois le scraping terminé, définissez un prix maximum (par exemple, 500€) et triez les produits par "Prix croissant".
5. Exportez les résultats en Excel si souhaité et visualisez la distribution des prix avec le graphique.

## Contributeurs

- [Mathieu Soussignan](https://www.mathieu-soussignan.com)

## Licence

Ce projet est sous licence MIT.
import streamlit as st
import pandas as pd
from src.scraping import run_scraping
import os
import time
import matplotlib.pyplot as plt
import io
from pandas import ExcelWriter

# Titre de l'application
st.title("Scraping Amazon avec Streamlit")
st.image("./assets/web-scraping.jpg", caption="L'art du scraping !", use_column_width=True)

# Sélecteur de catégorie
category = st.selectbox(
    "Choisissez une catégorie de produits :",
    ["smartphone", "ordinateur", "tablette", "télévision", "livres"]
)

# Construire l'URL en fonction de la catégorie choisie
URL = f"https://www.amazon.fr/s?k={category}"
# st.write("URL de scraping : ", URL)  # Débogage pour vérifier l'URL

# Fonction de scraping avec vérification de la création du fichier CSV
def fetch_data(url):
    # Supprimer l'ancien fichier CSV avant le nouveau scraping pour éviter les conflits
    if os.path.exists("data/produits_amazon.csv"):
        os.remove("data/produits_amazon.csv")
        print("Fichier CSV précédent supprimé.")

    # Lancer le scraping
    print("Démarrage du scraping...")
    run_scraping(url)
    
    # Vérifier si le fichier CSV a été généré
    if os.path.exists("data/produits_amazon.csv"):
        print("Fichier CSV créé avec succès.")  
        data = pd.read_csv("data/produits_amazon.csv")
        
        # Renommer les colonnes en fonction du nombre de colonnes dans le DataFrame
        column_count = len(data.columns)
        if column_count == 2:
            data.columns = ["Titre", "Prix"]
        elif column_count == 3:
            data.columns = ["Titre", "Prix", "Marque"]
        elif column_count == 4:
            data.columns = ["Titre", "Prix", "Marque", "URL_Image"]
        else:
            st.error("Le fichier CSV a un nombre de colonnes inattendu.")
        
        return data
    else:
        st.error("Le fichier CSV n'a pas été créé. Veuillez vérifier la fonction de scraping.")
        print("Le fichier CSV n'a pas été trouvé après le scraping.")
        return pd.DataFrame()  # Retourne un DataFrame vide si le fichier n'existe pas

# Bouton pour lancer le scraping
if st.button("Lancer le Scraping"):
    st.write(f"Le scraping de la catégorie '{category}' est en cours, veuillez patienter...")

    # Barre de progression
    progress_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.01)
        progress_bar.progress(percent_complete + 1)

    # Effectuer le scraping et charger les données dans st.session_state
    data = fetch_data(URL)
    if not data.empty:
        st.session_state[category] = data  # Stocke les données par catégorie dans l'historique
        st.success("Scraping terminé avec succès !")
        print("Données chargées dans st.session_state.")

# Vérifiez si des données sont présentes dans l'historique
if category in st.session_state:
    data = st.session_state[category]
    
    # Initialiser filtered_data
    filtered_data = data.copy()
    
    # Filtre de prix maximum
    max_price = st.slider("Filtrer les produits par prix maximum", min_value=0, max_value=1000, value=500)
    data["Prix"] = pd.to_numeric(data["Prix"], errors='coerce').fillna(0)
    filtered_data = filtered_data[filtered_data["Prix"] <= max_price]
    
    # Filtre de marque (si disponible)
    if "Marque" in data.columns:
        brand = st.selectbox("Filtrer par marque", options=["Toutes"] + list(data["Marque"].unique()))
        if brand != "Toutes":
            filtered_data = filtered_data[filtered_data["Marque"] == brand]
    
    # Tri des produits
    sort_option = st.selectbox("Trier par :", ["Prix croissant", "Prix décroissant", "Titre A-Z", "Titre Z-A"])
    if sort_option == "Prix croissant":
        filtered_data = filtered_data.sort_values(by="Prix")
    elif sort_option == "Prix décroissant":
        filtered_data = filtered_data.sort_values(by="Prix", ascending=False)
    elif sort_option == "Titre A-Z":
        filtered_data = filtered_data.sort_values(by="Titre")
    elif sort_option == "Titre Z-A":
        filtered_data = filtered_data.sort_values(by="Titre", ascending=False)

    # Afficher les résultats filtrés dans un tableau structuré
    st.write("Produits filtrés :")

    # Liste des colonnes disponibles dans le DataFrame
    columns_to_display = ["Titre", "Prix"]

    # Vérifiez si "Marque" et "URL_Image" existent avant de les ajouter à l'affichage
    if "Marque" in filtered_data.columns:
        columns_to_display.append("Marque")
    if "URL_Image" in filtered_data.columns:
        columns_to_display.append("URL_Image")

    # Afficher les données dans un tableau structuré avec les colonnes disponibles
    st.dataframe(filtered_data[columns_to_display].fillna("N/A"))

    # Exporter en fichier Excel
    if st.button("Exporter en Excel"):
        output = io.BytesIO()
        with ExcelWriter(output, engine='xlsxwriter') as writer:
            filtered_data.to_excel(writer, index=False, sheet_name="Produits")
        st.download_button(label="Télécharger Excel", data=output.getvalue(), file_name="produits_amazon.xlsx")

    # Afficher un graphique de distribution des prix
    fig, ax = plt.subplots()
    ax.hist(filtered_data["Prix"], bins=10, color="skyblue", edgecolor="black")
    ax.set_title("Distribution des prix")
    ax.set_xlabel("Prix (€)")
    ax.set_ylabel("Nombre de produits")
    st.pyplot(fig)
else:
    st.info("Cliquez sur 'Lancer le Scraping' pour démarrer.")
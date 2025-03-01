import streamlit as st
import pandas as pd
import joblib  # Pour charger un modèle pré-entraîné
import os


# === Configuration de la page ===
st.set_page_config(page_title="Visualisation du Modèle", layout="wide")

st.title("📊 Visualisation des Prédictions du Modèle")

# === Charger les données ===
DATA_PATH = "data/submission.csv"  # Mettez ici le chemin réel de votre fichier
MODEL_PATH = "data/submission.csv"  # Mettez ici le chemin réel de votre modèle
VISUALISATION_PATH = "data/submission.csv" # Mettez ici le chemin réel de votre fichier

# === Affichage des données et des prédictions côte à côte ===
col1, col2, col3 = st.columns(3)


# Vérifier si les chemins existent et charger les données et les prédictions
with col1:
    st.header("Données")
    if os.path.exists(DATA_PATH):
        df = pd.read_csv(DATA_PATH)
        st.write(df.head())
    else:
        st.error(f"❌ Le fichier {DATA_PATH} est introuvable !")
    # st.write(df)

with col2:
    st.header("Prédictions")
    if MODEL_PATH and os.path.exists(MODEL_PATH):
        model = pd.read_csv(MODEL_PATH)
        st.write(model.head())
    else:
        st.error(f"❌ Le modèle {MODEL_PATH} est introuvable ou non spécifié !")
with col3:
    st.header("Visualisation")
    if os.path.exists(VISUALISATION_PATH):
        visualisation = pd.read_csv(VISUALISATION_PATH)
        st.write(visualisation.head())
    else:
        st.error(f"❌ Le fichier {VISUALISATION_PATH} est introuvable !")


# === Affichage des graphiques ===
st.header("Graphiques")
st.write("Ici, vous pouvez afficher les graphiques de votre choix.")
# Ajoutez vos graphiques ici


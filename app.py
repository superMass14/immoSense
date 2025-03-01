import streamlit as st
import pandas as pd
import joblib  # Pour charger un modèle pré-entraîné
import os


# === Configuration de la page ===
st.set_page_config(page_title="ImmoSense", layout="centered", page_icon="🏠")

# === Centre de la page ===
st.markdown("<h2 style='text-align: center;'>🏠 Projet ImmoSense</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>📊  Visualisez les données et les prédictions du modèle ImmoSense.📊</p>", unsafe_allow_html=True)

# === Description du modele ===
st.header("Description du modèle")
st.write("When buyers describe their dream home, they often focus on aspects like the number of bedrooms or the presence of a garden. 🌳🏠 However, many hidden factors, such as basement height or proximity to a railway 🚂, also influence the final sale price. Through a vigorous analysis, we explain how these hidden factors impact the price. 🔍💡")
# Ajoutez votre description ici

# === Data exploration ===
st.header("Exploration des données")
st.write("Utilisez les données pour analyser les tendances et les inégalités dans les prix d'immobilier. ���️‍��️")



st.write("we will display the insights and highlight how the selected features are relevant for the sale price prediction. Features are categorized into nine(9) parts:")


inS1, inS2, inS3, inS4, inS5, inS6, inS7, inS8, inS9 = st.tabs(["General features", "Surfaces", "Garage", "Rooms and Bathrooms", "Quality", "Location", "Additional Value Features", "Sales Variables", "Created features"])

with inS1:
    st.header("General features")
    features = ["OverallQual", "OverallCond", "YearBuilt", "YearRemodAdd"]
    for feature in features:
        st.write(feature)
    st.write("Ces caractéristiques décrivent la qualité globale de la maison et son condition globale.")
    data = {
        "Feature": ["OverallQual", "OverallCond", "YearBuilt", "YearRemodAdd", "SalePrice"],
        "Correlation with SalePrice": [0.790982, -0.077856, 0.522897, 0.507101, 1.000000]
    }
    df_corr = pd.DataFrame(data)
    st.table(df_corr)
# Name: SalePrice, dtype: float64
with inS2:
    st.header("Surfaces")
    features = ["GrLivArea", "TotalBsmtSF", "LotArea"]
    for feature in features:
        st.write(feature)
    st.write("Ces caractéristiques décrivent la surface habitable de la maison.")
    data = {
        "Feature": ["GrLivArea", "TotalBsmtSF", "LotArea", "SalePrice"],
        "Correlation with SalePrice": [0.708624, 0.613581, 0.263843, 1.000000]
    }
    df_corr = pd.DataFrame(data)
    st.table(df_corr)
with inS3:
    st.header("Garage")
    features = ["GarageArea", "GarageCars", "GarageYrBlt", "GarageType", "GarageFinish"]
    for feature in features:
        st.write(feature)
    st.write("Ces caractéristiques décrivent l'emplacement et la condition du garage.")
    data = {
        "Feature": ["GarageArea", "GarageCars", "GarageYrBlt", "GarageType", "GarageFinish", "SalePrice"],
        "Correlation with SalePrice": [0.623431, 0.640409, 0.486362, 0.415283, 0.549247, 1.000000]
    }
    df_corr = pd.DataFrame(data)
    st.table(df_corr)
with inS4:
    st.header("Rooms and Bathrooms")
    features = ["FullBath", "HalfBath", "BedroomAbvGr", "KitchenAbvGr"]
    for feature in features:
        st.write(feature)
    st.write("Ces caractéristiques décrivent le nombre de chambres et salles de bain.")
    data = {
        "Feature": ["FullBath", "HalfBath", "BedroomAbvGr", "KitchenAbvGr", "SalePrice"],
        "Correlation with SalePrice": [0.560664, 0.284108, 0.168213, -0.135907, 1.000000]
    }
    df_corr = pd.DataFrame(data)
    st.table(df_corr)
with inS5:
    st.header("Quality")
    features = ["KitchenQual", "ExterQual", "ExterCond", "BsmtCond", "HeatingQC"]
    for feature in features:
        st.write(feature)
    st.write("Ces caractéristiques décrivent la qualité des matériaux utilisés.")
    data = {
        "Feature": ["KitchenQual", "ExterQual", "ExterCond", "BsmtCond", "HeatingQC", "SalePrice"],
        "Correlation with SalePrice": [0.659600, 0.682639, 0.018899, 0.212607, 0.427649, 1.000000]
    }
    df_corr = pd.DataFrame(data)
    st.table(df_corr)

    # === Prediction ===
    st.image("insight_plot/qualityPlot.png", use_column_width=True)
with inS6:
    st.header("Location")
    st.write("Neighborhood")
    st.write("MSZoning")
    st.write("Ces caractéristiques décrivent l'emplacement de la maison.")
    data = {
        "Feature": ["Neighborhood", "MSZoning", "SalePrice"],
        "Correlation with SalePrice": [0.413541, 0.125587, 1.000000]
    }
    df_corr = pd.DataFrame(data)
    st.table(df_corr)
    st.image('insight_plot/location.png', use_column_width=True) 
with inS7:
    st.header("Additional Value Features")
    features= ["Fireplaces", "FireplaceQu", "WoodDeckSF", "OpenPorchSF", "Foundation", "CentralAir"]
    for feature in features:
        st.write(feature)
    st.write("Ces caractéristiques décrivent les équipements et les installations supplémentaires.")
    data = {
        "Feature": ["Fireplaces", "FireplaceQu", "WoodDeckSF", "OpenPorchSF", "Foundation", "CentralAir", "SalePrice"],
        "Correlation with SalePrice": [0.466929, 0.520438, 0.324413, 0.315856, 0.382479, 0.251328, 1.000000]
    }
    df_corr = pd.DataFrame(data)
    st.table(df_corr)
with inS8:
    st.header("Sales Variables")
    st.write("SaleType")
    st.write("SaleCondition")
    st.write("MiscFeature")
    st.write("Ces caractéristiques décrivent les conditions de vente.")
    data = {
        "Feature": ["SaleType", "SaleCondition", "MiscFeature", "SalePrice"],
        "Correlation with SalePrice": [0.547509, 0.055898, 0.046953, 1.000000]
    }
    df_corr = pd.DataFrame(data)
    st.table(df_corr)
with inS9:
    st.header("Created features")
    st.write("Exterior")
    st.write("LifeSpan")
    st.write("Condition")
    st.write("Ces caractéristiques décrivent les caractéristiques supplémentaires de la maison.")   
    data = {
        "Feature": ["Exterior", "LifeSpan", "Condition", "SalePrice"],
        "Correlation with SalePrice": [0.587688, 0.431478, 0.289323, 1.000000]
    }
    df_corr = pd.DataFrame(data)
    st.table(df_corr)

    st.header("CentralAir vs SalePrice")
    data = {
        "CentralAir": ["N", "Y"],
        "count": [95, 1365],
        "sum": [10000087, 254144859]
    }
    df_central_air = pd.DataFrame(data)
    st.table(df_central_air)

# === Prédictions ===


# st.header("Prédictions")
# st.write("Voici les prédictions du modèle pour les données fournies.")
# st.write("Vous pouvez également visualiser les données et les prédictions côte à côte.")
# st.write("Vous pouvez également afficher les graphiques de votre choix.")
     


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


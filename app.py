import streamlit as st
import pandas as pd
import numpy as np
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

    st.header("Lifespan vs SalePrice")
    data = {
        "Lifespan": [1.00000, -0.52335],
        "SalePrice": [-0.52335, 1.00000]
    }
    df_lifespan = pd.DataFrame(data, index=["Lifespan", "SalePrice"])
    st.table(df_lifespan)

    st.header("CentralAir vs SalePrice")
    data = {
        "CentralAir": ["N", "Y"],
        "count": [95, 1365],
        "sum": [10000087, 254144859]
    }
    df_central_air = pd.DataFrame(data)
    st.table(df_central_air)

# === Prédictions ===

st.header("Prédictions")
st.write("Visualisez les données et les prédictions côte à côte pour comprendre comment le modèle fonctionne.")

tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])
data = np.random.randn(10, 1)

tab1.subheader("A tab with a chart")
tab1.image("insight_plot/qualityPlot.png")

tab2.subheader("A tab with the data")
tab2.write(data)


# === Affichage des graphiques ===
st.header("ImmoSense Models")

# Ajoutez vos graphiques ici

st.write("""
Let's pick the best model for our study case between:
- **Linear Regression**
- **SVR**
- **Ridge**
- **Nearest neighbors regression**
- **Decision trees**
""")

model = st.selectbox("Select the model", ["Linear Regression", "SVR", "Ridge", "Nearest neighbors regression", "Decision trees"])
st.write(f"Selected model: {model}")

# === Affichage des résultats ===

st.markdown("""
<style type="text/css">
#T_08cb6_row0_col0 {
  background-color: #4a63d3;
  color: #f1f1f1;
}
#T_08cb6_row0_col1, #T_08cb6_row1_col2, #T_08cb6_row2_col3, #T_08cb6_row3_col1, #T_08cb6_row4_col0 {
  background-color: #3b4cc0;
  color: #f1f1f1;
}
#T_08cb6_row0_col2 {
  background-color: #c53334;
  color: #f1f1f1;
}
#T_08cb6_row0_col3, #T_08cb6_row3_col3 {
  background-color: #edd1c2;
  color: #000000;
}
#T_08cb6_row1_col0, #T_08cb6_row1_col1, #T_08cb6_row4_col2, #T_08cb6_row4_col3 {
  background-color: #b40426;
  color: #f1f1f1;
}
#T_08cb6_row1_col3 {
  background-color: #5b7ae5;
  color: #f1f1f1;
}
#T_08cb6_row2_col0 {
  background-color: #de614d;
  color: #f1f1f1;
}
#T_08cb6_row2_col1 {
  background-color: #f3c7b1;
  color: #000000;
}
#T_08cb6_row2_col2 {
  background-color: #6788ee;
  color: #f1f1f1;
}
#T_08cb6_row3_col0 {
  background-color: #4055c8;
  color: #f1f1f1;
}
#T_08cb6_row3_col2 {
  background-color: #ba162b;
  color: #f1f1f1;
}
#T_08cb6_row4_col1 {
  background-color: #f5c2aa;
  color: #000000;
}
</style>
<table id="T_08cb6">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_08cb6_level0_col0" class="col_heading level0 col0" >RMSE</th>
      <th id="T_08cb6_level0_col1" class="col_heading level0 col1" >Mae</th>
      <th id="T_08cb6_level0_col2" class="col_heading level0 col2" >R2</th>
      <th id="T_08cb6_level0_col3" class="col_heading level0 col3" >Scores</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_08cb6_level0_row0" class="row_heading level0 row0" >Linear_regression</th>
      <td id="T_08cb6_row0_col0" class="data row0 col0" >46939.230000</td>
      <td id="T_08cb6_row0_col1" class="data row0 col1" >21099.120000</td>
      <td id="T_08cb6_row0_col2" class="data row0 col2" >0.671000</td>
      <td id="T_08cb6_row0_col3" class="data row0 col3" >0.900384</td>
    </tr>
    <tr>
      <th id="T_08cb6_level0_row1" class="row_heading level0 row1" >KNR</th>
      <td id="T_08cb6_row1_col0" class="data row1 col0" >54423.780000</td>
      <td id="T_08cb6_row1_col1" class="data row1 col1" >32000.570000</td>
      <td id="T_08cb6_row1_col2" class="data row1 col2" >0.558000</td>
      <td id="T_08cb6_row1_col3" class="data row1 col3" >0.791325</td>
    </tr>
    <tr>
      <th id="T_08cb6_level0_row2" class="row_heading level0 row2" >SVR</th>
      <td id="T_08cb6_row2_col0" class="data row2 col0" >53404.140000</td>
      <td id="T_08cb6_row2_col1" class="data row2 col1" >27773.890000</td>
      <td id="T_08cb6_row2_col2" class="data row2 col2" >0.575000</td>
      <td id="T_08cb6_row2_col3" class="data row2 col3" >0.766424</td>
    </tr>
    <tr>
      <th id="T_08cb6_level0_row3" class="row_heading level0 row3" >Ridge</th>
      <td id="T_08cb6_row3_col0" class="data row3 col0" >46696.640000</td>
      <td id="T_08cb6_row3_col1" class="data row3 col1" >21058.130000</td>
      <td id="T_08cb6_row3_col2" class="data row3 col2" >0.675000</td>
      <td id="T_08cb6_row3_col3" class="data row3 col3" >0.899800</td>
    </tr>
    <tr>
      <th id="T_08cb6_level0_row4" class="row_heading level0 row4" >Decision</th>
      <td id="T_08cb6_row4_col0" class="data row4 col0" >46512.010000</td>
      <td id="T_08cb6_row4_col1" class="data row4 col1" >27952.290000</td>
      <td id="T_08cb6_row4_col2" class="data row4 col2" >0.677000</td>
      <td id="T_08cb6_row4_col3" class="data row4 col3" >0.999996</td>
    </tr>
  </tbody>
</table>
""", unsafe_allow_html=True)


# === Affichage des graphiques ===
st.header("ImmoSense Models Visualization")
st.image("insight_plot/model_visiualisation.png")

st.write("""
The plot above shows how the model learns. The 'red dots' represent real data used for training. The 'blue line' represents the prediction.
The fluctuation highlights the model's error (over prediction/under prediction). Overall, we have a good fluctuation. We assume that ImmoSense is well trained.
""")


# === Affichage des poids des features ===
st.header("Feature's weight")
st.write("* Let's peek at **feature's weight**. This study will show us how each chosen feature **impacts** in the **model's precision**.")

html_code = """
<style type="text/css">
#T_9c7bc_row0_col0 {
  background-color: #3b4cc0;
  color: #f1f1f1;
}
#T_9c7bc_row1_col0 {
  background-color: #4961d2;
  color: #f1f1f1;
}
#T_9c7bc_row2_col0 {
  background-color: #5977e3;
  color: #f1f1f1;
}
#T_9c7bc_row3_col0 {
  background-color: #81a4fb;
  color: #f1f1f1;
}
#T_9c7bc_row4_col0 {
  background-color: #89acfd;
  color: #000000;
}
#T_9c7bc_row5_col0 {
  background-color: #e6d7cf;
  color: #000000;
}
#T_9c7bc_row6_col0 {
  background-color: #ead5c9;
  color: #000000;
}
#T_9c7bc_row7_col0 {
  background-color: #e36b54;
  color: #f1f1f1;
}
#T_9c7bc_row8_col0 {
  background-color: #b40426;
  color: #f1f1f1;
}
</style>
<table id="T_9c7bc">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_9c7bc_level0_col0" class="col_heading level0 col0" >Weigh</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_9c7bc_level0_row0" class="row_heading level0 row0" >Surfaces</th>
      <td id="T_9c7bc_row0_col0" class="data row0 col0" >88$</td>
    </tr>
    <tr>
      <th id="T_9c7bc_level0_row1" class="row_heading level0 row1" >General features</th>
      <td id="T_9c7bc_row1_col0" class="data row1 col0" >14970$</td>
    </tr>
    <tr>
      <th id="T_9c7bc_level0_row2" class="row_heading level0 row2" >Rooms and bathrooms</th>
      <td id="T_9c7bc_row2_col0" class="data row2 col0" >30840$</td>
    </tr>
    <tr>
      <th id="T_9c7bc_level0_row3" class="row_heading level0 row3" >Garage</th>
      <td id="T_9c7bc_row3_col0" class="data row3 col0" >66511$</td>
    </tr>
    <tr>
      <th id="T_9c7bc_level0_row4" class="row_heading level0 row4" >Additional feature value</th>
      <td id="T_9c7bc_row4_col0" class="data row4 col0" >73303$</td>
    </tr>
    <tr>
      <th id="T_9c7bc_level0_row5" class="row_heading level0 row5" >Sales variable</th>
      <td id="T_9c7bc_row5_col0" class="data row5 col0" >165330$</td>
    </tr>
    <tr>
      <th id="T_9c7bc_level0_row6" class="row_heading level0 row6" >Quality</th>
      <td id="T_9c7bc_row6_col0" class="data row6 col0" >169704$</td>
    </tr>
    <tr>
      <th id="T_9c7bc_level0_row7" class="row_heading level0 row7" >Location</th>
      <td id="T_9c7bc_row7_col0" class="data row7 col0" >262327$</td>
    </tr>
    <tr>
      <th id="T_9c7bc_level0_row8" class="row_heading level0 row8" >Created features</th>
      <td id="T_9c7bc_row8_col0" class="data row8 col0" >307113$</td>
    </tr>
  </tbody>
</table>
"""
st.markdown(html_code, unsafe_allow_html=True)

"""
Each coefficient represents the sample's increase effect (or decrease for negative coefficients) on the target (SalePrice).

In our case, if we take the `Rooms and bathrooms` category, we can say that, in general, each supplementary room or bathroom increases the house's price by **30,840$**. Same for the other categories.

What makes the features weight study more relevant is that we notice how the features we created influence the sales price. In fact, the more material the house is built with or the better the condition is, the more the sales price increases by **307,113$**.
"""

# === Final Prediction ===
st.header("Final Prediction")
df = pd.read_csv("data/submission.csv")

st.table(df.head())

st.write("""
The final prediction is shown in the table above.

Remember that this model is still a simplified version and might not be the best choice for real-world applications. However, it serves as a starting point for further analysis and improvements.
""")

# === Footer ===
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>🏠 Projet ImmoSense - JARVIS TEAM 🏠</p>", unsafe_allow_html=True)

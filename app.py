import streamlit as st
import pandas as pd
import numpy as np


# === Configuration de la page ===
st.set_page_config(page_title="ImmoSense", layout="centered", page_icon="🏠")

# === Centre de la page ===
st.markdown("<h2 style='text-align: center;'>🏠 ImmoSense</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>📊  Visualize data and model performane 📊</p>", unsafe_allow_html=True)

# === Description du modele ===
st.title("Project overview")
st.write("""
        When buyers describe their dream home, they often focus on aspects like the number of bedrooms or the presence of a garden.
        🌳🏠 However, many hidden factors, such as basement height or proximity to a railway 🚂, 
        also influence the final sale price. Through a vigorous analysis, 
        we explain how these hidden factors impact the price. 🔍💡
        """)
# Ajoutez votre description ici

# === Data exploration ===
st.title("1️⃣ Data exploration 🔍")
st.write("""
        Relevant features have been categorized into nine(9) parts. click to check insights
        """)


inS1, inS2, inS3, inS4, inS5, inS6, inS7, inS8, inS9 = st.tabs(["General features", "Surfaces", "Garage", "Rooms and Bathrooms", "Quality", "Location", "Additional Value Features", "Sales Variables", "Created features"])

with inS1:
    st.subheader("General features")
    features= [
                      "OverallQual (Overall quality)", 
                      "OverallCond (Overall condition)", 
                      "YearBuilt (Year built)", 
                      "YearRemodAdd (Year of renovation)"
                      ]
    
    d, tab1 = st.tabs(["🗄️ data", "📈 chart"])
    with d:
      data = {
          "Feature": [
                      "OverallQual (Overall quality)", 
                      "OverallCond (Overall condition)", 
                      "YearBuilt (Year built)", 
                      "YearRemodAdd (Year of renovation)",
                      "SalePrice (Sale price)"
                      ],
          "Correlation with SalePrice": [0.790982, -0.077856, 0.522897, 0.507101, 1.000000]
      }
      df_corr = pd.DataFrame(data)
      st.table(df_corr)
    with tab1:
      tab1.image("insight_plot/general.png")
      tab1.write("""
We started with features that would be of most interest to potential customers, known as ‘general features’: **overall condition**, **overall quality**, **year of construction** and **year of remode**l.
Calculating the correlation between these features and the saleprice shows that the **stronger** OverallQual is, the **higher** the price. With an average correlation of YearBuilt and YearRemodAdd , newer homes tend to be more expensive. And finally, OverallCond has an opposite influence on price.
""")
# Name: SalePrice, dtype: float64
with inS2:
    st.header("Surfaces")
    data = {
        "Feature": [
    "GrLivArea (Living area)", 
    "TotalBsmtSF (Total basement area)", 
    "LotArea (Lot area)",
    "SalePrice (Sale price)"
],
        "Correlation with SalePrice": [0.708624, 0.613581, 0.263843, 1.000000]
    }

    df_corr = pd.DataFrame(data)
    d2, tab2 = st.tabs(["🗄️ data", "📈 chart"])
    with d2:
      st.table(df_corr)
    with tab2:
      tab2.image("insight_plot/surface.png")
      tab2.write("Second interesting point, the surface area! this combines the above-ground living area, the total surface area in square feet of the basement and the surface area of the plot in square feet. this shows that the price increases with the surface area (trend in red).")


with inS3:
    st.header("Garage")
    features = [
    "GarageArea (Garage area)", 
    "GarageCars (Garage capacity in cars)", 
    "GarageYrBlt (Year garage was built)", 
    "GarageType (Garage type)", 
    "GarageFinish (Garage finish)",
    "SalePrice (Sale price)"
]
    data = {
        "Feature": features,
        "Correlation with SalePrice": [0.623431, 0.640409, 0.486362, 0.415283, 0.549247, 1.000000]
    }
    df_corr = pd.DataFrame(data)
    d3, tab3 = st.tabs(["🗄️ data", "📈 chart"])
    with d3:
      st.table(df_corr)
    with tab3:
      tab3.subheader("📈 Garage")
      tab3.image("insight_plot/garage.png")
      tab3.image("insight_plot/garage1.png")
      tab3.write("""
We are now interested in the **‘garage’** criterion, which brings together all the attributes linked to the garage: its surface area, its capacity, its year of construction, its type and its finish.
After a study of the correlation for some of these attributes, we were able to see that GarageYrBlt has a fairly weak impact on price, but it has a strong influence on GarageArea and GarageCars, which in turn influence price.

We also found that **GarageType** and **GarageFinish** had an impact on the price. For example, a garage of type BuiltIn and completely finished would give the house a very high price.
""")

with inS4:
    st.header("Rooms and Bathrooms")
    data = {
        "Feature": [
    "FullBath (Full bathrooms)", 
    "HalfBath (Half bathrooms)", 
    "BedroomAbvGr (Bedrooms above ground)", 
    "KitchenAbvGr (Kitchens above ground)",
    "SalePrice (Sale price)"
],
        "Correlation with SalePrice": [0.560664, 0.284108, 0.168213, -0.135907, 1.000000]
    }
    df_corr = pd.DataFrame(data)
    df_corr = pd.DataFrame(data)
    d4, tab4 = st.tabs(["🗄️ data", "📈 chart"])
    with d4:
      st.table(df_corr)
    
    with tab4:
      tab4.image("insight_plot/rooms_bathrooms.png")
      tab4.write("""
      The **number of bedrooms** and the **presence of bathrooms** *(full or not)* are criteria that some buyers are very particular about, and they are grouped together in Bedrooms and Bathrooms: full bathrooms, half-bathrooms, above-ground bedrooms and above-ground kitchens. With the correlation study it is clear that in general the presence of FullBath has a clear influence on price where the others *(HalfBath ,BedroomAbvG ,KitchenAbvGr)* vary, showing that they depend on other criteria to be influential.
      """)
      
with inS5:
    st.header("Quality")
    features = [
    "KitchenQual (Kitchen quality)", 
    "ExterQual (Exterior quality)", 
    "ExterCond (Exterior condition)", 
    "BsmtCond (Basement condition)", 
    "HeatingQC (Heating quality)",
    "SalePrice (Sale price)"
]
    data = {
        "Feature": features,
        "Correlation with SalePrice": [0.659600, 0.682639, 0.018899, 0.212607, 0.427649, 1.000000]
    }
    df_corr = pd.DataFrame(data)
    d5, tab5 = st.tabs(["🗄️ data", "📈 chart"])
    with d5:
      st.table(df_corr)
    with tab5:
      tab5.image("insight_plot/qualityPlot.png")
      tab5.write("Here we merged Kitchen's quality, Exterior's quality and condition, basement's condition and heating quality to get the building's comfort average quality. Values have been encoded ordinally. We notice that have high price sale prices within the range of 3-4.5 (good to excellent). meanwhile houses with poor to fair quality or without one these conveniences have lower prices. We conclude having good conviences quality can influence the house's sale price")

with inS6:
    st.header("Location")
    st.write("Neighborhood")
    st.write("MSZoning")
    data = {
        "Feature": [
    "Neighborhood (Neighborhood)", 
    "MSZoning (Zoning)",
    "SalePrice (Sale price)"
],
        "Correlation with SalePrice": [0.413541, 0.125587, 1.000000]
    }
    df_corr = pd.DataFrame(data)
    d6, tab6 = st.tabs(["🗄️ data", "📈 chart"])
    with d6:
      st.table(df_corr)
    with tab6:
      tab6.subheader("📈 Location")
      tab6.image("insight_plot/location.png")
      tab6.write("Plots aboves display prices variations depending on the area and the zone. These two are relevant feature allows us to understand the houses's price increase and decrease")

with inS7:
    st.header("Additional Value Features")
    features= [
    "Fireplaces (Number of fireplaces)", 
    "FireplaceQu (Fireplace quality)", 
    "WoodDeckSF (Wood deck area)", 
    "OpenPorchSF (Open porch area)", 
    "Foundation (Foundation type)", 
    "CentralAir (Central air conditioning)",
    "SalePrice (Sale price)"
]

    data = {
        "Feature": features,
        "Correlation with SalePrice": [0.466929, 0.520438, 0.324413, 0.315856, 0.382479, 0.251328, 1.000000]
    }
    df_corr = pd.DataFrame(data)
    
    d7, tab7 = st.tabs(["🗄️ data", "📈 chart"])
    with d7:
      st.table(df_corr)
    with tab7:
      tab7.image("insight_plot/additional_value.png")
      tab7.image("insight_plot/Fireplace.png")
      tab7.write("""
      The foundation used for construction are also important when someone buys a house. The plot highlights the preference of buying a house built with **poured concrete** *(pconc)* followed the by ones built with **wood** and **stone**. This phenomenon are explain by the fact that the house is more likely to be solid with such foundations. Hence **slab** built house's have lower prices. 
      House's with excellent ***(ex)*** quality, even good are more valuable than ones with poor quality or without fireplace. This convenience can be a good feature for the model.
      """)
      
with inS8:
    st.header("Sales Variables")
    data = {
        "Feature": [
    "SaleType (Sale type)", 
    "SaleCondition (Sale condition)", 
    "MiscFeature (Miscellaneous features not detailed)",
    "SalePrice (Sale price)"
],
        "Correlation with SalePrice": [0.547509, 0.055898, 0.046953, 1.000000]
    }
    df_corr = pd.DataFrame(data)
    d8, tab8 = st.tabs(["🗄️ data", "📈 chart"])
    with d8:
      st.table(df_corr)
    with tab8:
      tab8.image("insight_plot/saleVPlot.png")
      tab8.write("""
      We notice that houses sold:
      - after just being constructed and sold *(new)*,
      - with a  Low Down payment contract and low interest *(ConLw)*
      - with a Warranty Deed - Cash *(CWD)*
      are the top **3** valuable in our dataset. The more varied the sale type is, the more disproportion we have in the house prices
      """)
      
with inS9:
    st.header("Created features")
    data = {
        "Feature": [
    "Exterior (Combination of Exterior1 and Exterior2)", 
    "Condition (Condition1 + Condition2)", 
    "LifeSpan (Age of the house)",
    "SalePrice (Sale price)"
],
        "Correlation with SalePrice": [0.587688, 0.431478, 0.289323, 1.000000]
    }
    df_corr = pd.DataFrame(data)
    d9, tab9 = st.tabs(["🗄️ data", "📈 chart"])
    with d9:
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
    with tab9:
      tab9.image("insight_plot/created_features.png")
      tab9.write("""
      In order to study the relation between the **sale price** and the **exterior** covering combined with the proximity to various **conditions**, we've encoded the categorical values using the `One-hot encoder` model then perfom a **correlation computation**.
      In this context, the small values do not reveal a no relationship between the features and the sale price but how each category influence the price. Some causes the prices to increase, other do the opposite.
      """)



# === Affichage des graphiques ===
st.title("2️⃣ Model selection")

# Ajoutez vos graphiques ici

st.write("""
Let's pick the best model for our study case between.
pick a model to check performance
""")

model = st.multiselect("Select the model", ["Linear Regression", "SVR", "Ridge", "Nearest neighbors regression", "Decision trees"])

st.table(pd.read_csv("insight_plot/model_perf.csv", index_col="model").loc[model, :])

# === Affichage des résultats ===



# === Affichage des graphiques ===
st.title("3️⃣ 🏠 ImmoSense model visualization" )
st.image("insight_plot/model_visiualisation.png")

st.markdown("""
after analyzing the performances, ImmoSense's model is : `Ridge_regression`.
The plot above shows how the model learns. The 'red dots' represent real data used for training. The 'blue line' represents the prediction.
The fluctuation highlights the model's error (over prediction/under prediction). Overall, we have a good fluctuation. We assume that ImmoSense is well trained.
""")


# === Affichage des poids des features ===
st.title("4️⃣ 🏋🏽‍♂️ Feature's weight")
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

# === Footer ===
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>🏠 ImmoSense - JARVIS TEAM 🏠</p>", unsafe_allow_html=True)

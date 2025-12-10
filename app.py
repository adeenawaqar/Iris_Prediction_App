import streamlit as st
import pandas as pd

st.title("🌸Iris Flower Species Prediction🌸")

# Load dataset (optional – for display)
iris = pd.read_csv("IRIS dataset.csv")

st.sidebar.header("Input Features")

sepal_length = st.sidebar.number_input(
    "Sepal Length (cm)", 0.0, 10.0, 5.0
)
sepal_width = st.sidebar.number_input(
    "Sepal Width (cm)", 0.0, 10.0, 3.5
)
petal_length = st.sidebar.number_input(
    "Petal Length (cm)", 0.0, 10.0, 1.4
)
petal_width = st.sidebar.number_input(
    "Petal Width (cm)", 0.0, 10.0, 0.2
)

if st.button("Predict"):
    # RULE-BASED formula (works very well for Iris)
    if petal_length < 2:
        species = "Iris-setosa"
    elif petal_length < 5:
        species = "Iris-versicolor"
    else:
        species = "Iris-virginica"

    st.success(f"Predicted Iris Species: **{species}**")


import streamlit as st
import pandas as pd

st.title("🌸 Iris Flower Species Prediction (Streamlit + Pandas) 🌸")

# Just creating a DataFrame from user input (file handling NOT used)
st.sidebar.header("Input Features")

sepal_length = st.sidebar.number_input("Sepal Length (cm)", 0.0, 10.0, 5.0)
sepal_width  = st.sidebar.number_input("Sepal Width (cm)", 0.0, 10.0, 3.5)
petal_length = st.sidebar.number_input("Petal Length (cm)", 0.0, 10.0, 1.4)
petal_width  = st.sidebar.number_input("Petal Width (cm)", 0.0, 10.0, 0.2)

# Create a Pandas DataFrame (WITHOUT reading any file)
input_df = pd.DataFrame({
    "sepal_length": [sepal_length],
    "sepal_width": [sepal_width],
    "petal_length": [petal_length],
    "petal_width": [petal_width]
})

st.write("📌 Your Input Data (Pandas DataFrame):")
st.dataframe(input_df)

if st.button("Predict"):
    # Simple logic-based prediction
    if petal_length < 2:
        species = "Iris-setosa"
    elif petal_length < 5:
        species = "Iris-versicolor"
    else:
        species = "Iris-virginica"

    st.success(f"Predicted Iris Species: **{species}**")

import streamlit as st
import pickle
import pandas as pd

with open('knn_iris_model.pkl', 'rb') as f:
    knn = pickle.load(f)

with open('label_encoder.pkl', 'rb') as f:
    le = pickle.load(f)

st.title("🌸Iris Flower Species Prediction🌸")

st.sidebar.header("Input Features")
sepal_length = st.sidebar.number_input("Sepal Length (cm)", min_value=0.0, max_value=10.0, value=5.0)
sepal_width = st.sidebar.number_input("Sepal Width (cm)", min_value=0.0, max_value=10.0, value=3.5)
petal_length = st.sidebar.number_input("Petal Length (cm)", min_value=0.0, max_value=10.0, value=1.4)
petal_width = st.sidebar.number_input("Petal Width (cm)", min_value=0.0, max_value=10.0, value=0.2)

input_data = pd.DataFrame([[sepal_length, sepal_width, petal_length, petal_width]],
                          columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])
if st.button("Predict"):
    pred = knn.predict(input_data)
    species = le.inverse_transform(pred)[0]
    st.success(f"The predicted Iris species is: **{species}**")

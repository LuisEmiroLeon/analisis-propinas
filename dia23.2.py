import streamlit as st
import joblib

model = joblib.load('modelo_propinas.pkl')

st.title("🤖 Predictor de Propinas - Tu IA")
bill = st.number_input("Total de la cuenta ($)", 3, 100, 20)
size = st.slider("Personas", 1, 6, 2)

if st.button("Predecir propina"):
    # size, sex, smoker por defecto para demo
    pred = model.predict([[bill, size, 1, 0]])
    st.success(f"Propina estimada: ${pred[0]:.2f}")
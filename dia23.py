import pandas as pd
import streamlit as st
import joblib

# Carga tu modelo ganador R² 0.4485
model = joblib.load('modelo_propinas.pkl')

st.title("🤖 Predictor de Propinas")
st.write("Tu primera IA - Modelo LinearRegression R² 0.4485")

bill = st.number_input("Total de la cuenta ($)", min_value=3.0, max_value=100.0, value=20.0)
size = st.slider("Número de personas", 1, 6, 2)
sex = st.selectbox("Sexo", ["Male", "Female"])
smoker = st.selectbox("Fumador", ["No", "Yes"])

sex_code = 1 if sex =="Male" else 0
smoker_code = 1 if smoker =="Yes" else 0

if st.button("Predecir propina"):

    input_data = pd.DataFrame([[bill, size, sex_code, smoker_code]], columns=["total_bill", "size", "sex_code", "smoker_code"])
    pred = model.predict(input_data)
    st.success(f"💰 Propina estimada: ${pred[0]:.2f}")
    st.balloons()
    st.caption(f"Inputs: bill={bill}, size={size}, sex={sex}({sex_code}), smoker={smoker}({smoker_code})")
# Correr Streamlit con "py -m streamlit run app.py"
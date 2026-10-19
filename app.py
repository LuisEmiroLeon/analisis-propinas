import pandas as pd
import streamlit as st
import joblib
# Carga modelo ganador 0.4675
model = joblib.load('modelo_propinas.pkl')
st.title("🤖 Predictor de Propinas - R² 0.4675")
st.caption("Modelo 6 columnas: total_bill + size + day_Fri/Sat/Sun + time_Dinner")
bill = st.number_input("Total cuenta ($)", 3.0, 100.0, 20.0)
size = st.slider("Personas en la mesa", 1, 6, 2)
day = st.selectbox("Día", ["Thur","Fri","Sat","Sun"])
time = st.selectbox("Momento", ["Lunch","Dinner"])
# Mapeo exacto a tus 6 columnas ganadoras
day_Fri = 1 if day == "Fri" else 0
day_Sat = 1 if day == "Sat" else 0
day_Sun = 1 if day == "Sun" else 0
time_Dinner = 1 if time == "Dinner" else 0
if st.button("💰 Predecir propina"):
    data = pd.DataFrame([[bill, size, day_Fri, day_Sat, day_Sun, time_Dinner]],
                        columns=["total_bill","size","day_Fri","day_Sat","day_Sun","time_Dinner"])
    pred = model.predict(data)
    st.success(f"Propina estimada: ${pred[0]:.2f}")
    st.balloons()
    # Correr Streamlit con "py -m streamlit run app.py"
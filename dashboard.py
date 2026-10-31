import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

DB_NAME = "propinas.db"

st.set_page_config(page_title="Dashboard Propinas R² 0.4675", layout="wide")
st.title("📊 Dashboard Propinas - Modelo Ganador R² 0.4675")
st.caption("API: luisemiro/api-propinas | Streamlit: predecir-propinas-luis")

def cargar_datos():
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query("SELECT * FROM predicciones ORDER BY id DESC", conn)
    conn.close()
    return df

try:
    df = cargar_datos()

    if df.empty:
        st.warning("No hay predicciones aún. Haz POST /predict en tu API")
    else:
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Predicciones", len(df))
        with col2:
            st.metric("Propina Promedio", f"${df['propina_estimada'].mean():.2f}")
        with col3:
            st.metric("Ticket Promedio", f"${df['total_bill'].mean():.2f}")
        with col4:
            st.metric("R² Modelo", "0.4675")

        st.divider()

        col_a, col_b = st.columns(2)
        with col_a:
            st.subheader("Propinas por Día")
            fig = px.bar(df, x="day", y="propina_estimada", color="day", title="Propina estimada por día")
            st.plotly_chart(fig, use_container_width=True)

        with col_b:
            st.subheader("Relación Cuenta vs Propina")
            fig2 = px.scatter(df, x="total_bill", y="propina_estimada", color="time", size="size", title="Total Bill vs Propina")
            st.plotly_chart(fig2, use_container_width=True)

except Exception as e:
    st.error(f"No se pudo cargar DB: {e}")
    st.info("Asegúrate que propinas.db existe. Corre python database.py")
   
    # Correr Streamlit con "py -m streamlit run dashboard.py"
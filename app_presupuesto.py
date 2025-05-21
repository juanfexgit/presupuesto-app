import streamlit as st
import pandas as pd

st.title("Presupuesto Juan Fer - 2025")

archivo = 'Presupuesto juan fer - 2025.xlsx'

# Obtener los nombres de las hojas
hojas = pd.ExcelFile(archivo).sheet_names

# Menú desplegable para elegir hoja
hoja_seleccionada = st.selectbox("Selecciona una hoja", hojas)

# Leer solo la hoja seleccionada
df = pd.read_excel(archivo, sheet_name=hoja_seleccionada)

# Mostrar los datos
st.subheader(f"Datos de la hoja: {hoja_seleccionada}")
st.dataframe(df)

# Mostrar total si hay una columna llamada "Monto"
if 'Monto' in df.columns:
    total = df['Monto'].sum()
    st.write(f"**Total:** ${total:,.0f}")
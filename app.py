import streamlit as st
import pandas as pd

def generar_estadisitcas(df):

    """
    Genera Estadistica descriptivas de un dataframe
    """

    return df.describe()

def exportar_excel(df):
    """
    Exporta un dataframe a un archivo excel
    """

    with open("Estadisticas_descriptivas.xlsx.", "wb") as archivo:
        df.to_excel(archivo, index=False, sheet_name= "Estadisticas")
       
        return "Estadisticas_descriptivas.xlsx."

st.title("Analizador de  Archivos Excel o Csv")

archivo_subido = st.file_uploader("Sube tu archivo Excel o Csv", type = ["xlsx", "xls", "csv"])

if archivo_subido is not None: 
    st.write("El archivo ha sido cargado")
    if archivo_subido.name.endswith("csv"):
        df = pd.read_csv(archivo_subido)
    else:
        df = pd.read_excel(archivo_subido)
    st.write("###DataFrame Original")
    st.dataframe(df)

    df_estadisticas = generar_estadisitcas(df)
    st.dataframe(df_estadisticas)

    ruta_archivo = exportar_excel( df_estadisticas)
    
    with open(ruta_archivo, "rb") as archivo:
        st.download_button(
            label = "Descargar Estadisticas en Excel",
            data = archivo,
            file_name= "Estadisticas_descriptvas.xlsx",
            mime="application/vnd.openxmlformats-officedument.spreadsheetml.sheet"


        )
else:
    st.write("Por favor cargar el archivo")

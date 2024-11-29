import streamlit as st 
from prediksi_penyakit_ginjal import load_data

from Tabs import home, predict, visualise

def show_dataset(df):
    st.header("Dataset Penyakit Ginjal")
    st.write("Halaman ini memuat dataset yang digunakan untuk melatih model.")
    st.dataframe(df)
    
Tabs = {
    "Beranda" : home,
    "Prediksi" : predict,
    "Visualisasi" : visualise
}

st.sidebar.title("Navigasi")

page = st.sidebar.radio("Pages", list(Tabs.keys()))

df, x, y = load_data()

if page == "Prediksi":
    show_dataset(df)
    Tabs[page].app(df, x, y)
elif page == "Visualisasi":
    Tabs[page].app(df, x, y)
else: 
    Tabs[page].app()
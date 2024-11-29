import streamlit as st
import pandas as pd

from prediksi_penyakit_ginjal import predict

def show_dataset():
    st.header("Dataset Penyakit Ginjal")
    st.write("Halaman ini memuat dataset yang digunakan untuk melatih model.")
    
    # Membaca dataset
    try:
        df = pd.read_csv("kidney-disease.csv")
        st.dataframe(df)
    except FileNotFoundError:
        st.error("File dataset tidak ditemukan. Pastikan file 'kidney-disease.csv' tersedia di direktori.")

def app(df, x, y):
    
    st.title("Halaman Prediksi")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        bp = st.text_input('Input Nilai bp', '80.0')  # Tekanan darah
    with col1:
        sg = st.text_input('Input Nilai sg', '1.02')  # Specific Gravity
    with col1:
        al = st.text_input('Input Nilai al', '1.0')  # Albumin
    with col1:
        su = st.text_input('Input Nilai su', '0.0')  # Gula
    with col1:
        rbc = st.text_input('Input Nilai rbc', '1')  # Sel darah merah
    with col1:
        pc = st.text_input('Input Nilai pc', '1')  # Sel epitel pipih
    with col1:
        pcc = st.text_input('Input Nilai pcc', '0')  # Sel epitel abnormal
    with col1:
        ba = st.text_input('Input Nilai ba', '0')  # Bakteri
    with col2:
        bgr = st.text_input('Input Nilai bgr', '121.0')  # Glukosa darah
    with col2:
        bu = st.text_input('Input Nilai bu', '36.0')  # Urea darah
    with col2:
        sc = st.text_input('Input Nilai sc', '1.2')  # Serum Kreatinin
    with col2:
        sod = st.text_input('Input Nilai sod', '138.0')  # Natrium
    with col2:
        pot = st.text_input('Input Nilai pot', '4.4')  # Kalium
    with col2:
        hemo = st.text_input('Input Nilai hemo', '15.4')  # Hemoglobin
    with col2:
        pcv = st.text_input('Input Nilai pcv', '32')  # Packed Cell Volume
    with col2:
        wc = st.text_input('Input Nilai wc', '72')  # Sel darah putih
    with col3:
        rc = st.text_input('Input Nilai rc', '34')  # Sel darah merah
    with col3:
        htn = st.text_input('Input Nilai htn', '1')  # Hipertensi
    with col3:
        dm = st.text_input('Input Nilai dm', '4')  # Diabetes Mellitus
    with col3:
        cad = st.text_input('Input Nilai cad', '1')  # Penyakit arteri koroner
    with col3:
        appet = st.text_input('Input Nilai appet', '0')  # Nafsu makan
    with col3:
        pe = st.text_input('Input Nilai pe', '0')  # Edema pedal
    with col3:
        ane = st.text_input('Input Nilai ane', '0') # Anemia
        
    features = [bp,sg,al,su,rbc,pc,pcc,ba,bgr,bu,sc,sod,pot,hemo,pcv,wc,rc,htn,dm,cad,appet,pe,ane]
    
    if st.button("Prediksi"):
        prediction, score = predict(x,y,features)
        score = score
        st.info("Prediksi Sukses...")
        
        if (prediction == 1):
            st.warning("Orang tersebut rentan terkena penyakit ginjal")
        else:
            st.success("Orang tersebut relatif aman dari penyakit ginjal")
            
        st.write("Model yang digunakan memiliki tingkat akurasi ", (score*100),"%")
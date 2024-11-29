import streamlit as st

def app():
    st.title("Aplikasi Prediksi Penyakit Batu Ginjal")
    st.write(
        "<div style='text-align: justify;'>"
        "Aplikasi ini menggunakan model Decision Tree untuk memprediksi penyakit ginjal pada seseorang berdasarkan beberapa data seperti tekanan darah (bp), gravitasi spesifik urin (sg), kadar albumin (al), dan gula (su). "
        "Aplikasi ini dirancang untuk membantu memahami hubungan antar variabel data dan memprediksi penyakit ginjal dengan cepat dan akurat."
        "</div>",
        unsafe_allow_html=True,
    )
    st.write("Dibuat oleh Natasya Inge Nugroho")
    
    st.markdown(
        """
        Dataset yang digunakan dalam aplikasi ini dapat diakses di [Kaggle - Chronic Kidney Disease Dataset](https://www.kaggle.com/datasets/mansoordaku/ckdisease).
        """
    )

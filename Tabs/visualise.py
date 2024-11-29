import warnings
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
from sklearn import tree
import streamlit as st

from prediksi_penyakit_ginjal import train_model

def app(df, x, y):
    warnings.filterwarnings('ignore')
    st.set_option('deprecation.showPyplotGlobalUse', False)

    st.title("Visualisasi Prediksi Batu Ginjal")

    # Split data menjadi training dan testing
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    
    if st.checkbox("Plot Confusion Matrix"):
        model, score = train_model(x_train, y_train)
        plt.figure(figsize=(10, 6))
        
        # Gunakan ConfusionMatrixDisplay
        ConfusionMatrixDisplay.from_estimator(
            estimator=model,
            X=x_test,
            y=y_test,
            display_labels=['nockd', 'ckd'],
            values_format='d',
            cmap='Blues'
        )
        st.pyplot()

    if st.checkbox("Plot Decision Tree"):
        model, score = train_model(x_train, y_train)
        dot_data = tree.export_graphviz(
            decision_tree=model, max_depth=4, out_file=None, filled=True, rounded=True,
            feature_names=x.columns, class_names=['nockd', 'ckd']
        )
        st.graphviz_chart(dot_data)

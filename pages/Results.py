import streamlit as st
import pandas as pd
from Stream_GBM import ui_analysis
from pages import Analysis


#dataset visualization function
def data_visualizaton():
    st.markdown('---')
    st.subheader('1. Dataset Visualization')
    
    #show data-distribution
    st.caption('Data Distribution')
    st.image('./figures/hist_subplot.png')


#download predicted csv
def download(upload_csv):
    st.markdown('---')
    st.subheader('3. Download Results')
    
    upload_csv = upload_csv.to_csv()
    st.download_button(
    "Press to Download",
    upload_csv,
    "Predicted_SoilTypes.csv",
    "text/csv",
    key='download-csv'
    )


def main():
    ui_analysis()
    
    data_visualizaton()
    
    #show accuracy and confusion matrix
    st.markdown('---')
    st.subheader('2. Accuracy & Confusion Matrix')
    st.image('./figures/Confusion_matrix.png')
    
    st.markdown('---')
    st.subheader('3. Feature importances')
    st.image('./figures/importance.png')


if __name__ == '__main__':
    main()
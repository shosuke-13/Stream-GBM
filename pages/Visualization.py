import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from Stream_GBM import ui_analysis
from pages import Analysis

def make_hist(dataset,dataset_column):

    # visualize 1 column data
    if dataset[dataset_column].dtype != object:
        
        # plot histgram and kde
        dataset[dataset_column].plot.hist(alpha=0.5,legend=True)
        dataset[dataset_column].plot.kde(alpha=0.5,legend=True, secondary_y=True)
        
        st.pyplot(plt)


def select_column(dataset):
    
    # select column you want to visualize
    st.caption('Select a column you want to visualize.')
    
    # select box : select a dataset column
    dataset_column = st.selectbox('Select a Column',dataset.columns.values,label_visibility="hidden")
    st.write(dataset_column)
    
    return dataset_column


def main():
    ui_analysis()
    dataset = Analysis.upload()
    
    # check csv file uploaded
    if dataset is not None:
        st.markdown('### Descriptive Statistics')
        
        # make descriptive statistics table
        dataset_statics = dataset.describe().to_csv()
        
        # download descriptive statistic csv file
        st.download_button( "Press to Download",
                            dataset_statics,
                            "dataset_statics.csv",
                            "text/csv",
                            key='download-csv' )
        # view descriptive statistics table
        st.write(dataset.describe())
        
        st.markdown('### Histgram and kernel density estimation')
        dataset_column = select_column(dataset)
        
        make_hist(dataset,dataset_column)
        

if __name__ == '__main__':
    main()
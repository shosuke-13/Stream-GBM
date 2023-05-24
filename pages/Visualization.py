import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from main import ui_analysis
from modules import file_uploader


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
    input = file_uploader.upload()
    #dataset = pd.read_csv(input)
    # check csv file uploaded
    if input is not None :
        dataset = pd.DataFrame(input)
        
        st.markdown("#### Visualize your dataset")
        
        # analysis section 1
        descriptive, histgram, correlation = st.tabs(['Descriptive Statistics',
                                                      'Histgram and kernel density estimation', 
                                                      'Correlation matrix'])
        with descriptive:
            # make descriptive statistics table
            dataset_statics = dataset.describe().to_csv()
            
            # view descriptive statistics table
            st.write(dataset.describe())
            
            # download descriptive statistic csv file
            st.download_button( "Press to Download",
                                dataset_statics,
                                "dataset_statics.csv",
                                "text/csv",
                                key='download-csv' )

        with correlation:
            st.markdown('### Correlation matrix')
            corr = dataset.corr()
            plt.figure(figsize=(12,12))
            sns.heatmap(corr,square = True,vmax=1,vmin=-1,center=0,cmap='cool')
            st.pyplot(plt)
            
        with histgram:
            st.markdown('### Histgram and kernel density estimation')
            dataset_column = select_column(dataset)
            
            make_hist(dataset,dataset_column)
            

if __name__ == '__main__':
    main()
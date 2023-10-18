import pandas as pd
import streamlit as st
import pygwalker as pyg
from main import ui_analysis
 
st.set_page_config(layout="wide", page_icon="🧊")


def default_dashboard():
    sample = pd.read_csv('sample/sample_dataset.csv')
    
    # Graphic Walker
    if sample is not None:
        sample_output = pyg.walk(sample, env='Streamlit')
        st.write(sample_output)

 
def main():
    ui_analysis()
    st.markdown("## - EDA using PyGwalker -")
    st.info("Visualization your dataset using PyGwalker", icon="ℹ️")
    st.markdown("---")
    
    st.write(':sunglasses: Default dataset is sample. Please upload your dataset')
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
                
        output = pyg.walk(df, env='Streamlit')
        st.write(output)
        
        if st.button('Show default dataset'): default_dashboard()
            
    else : default_dashboard()
    
    st.markdown("---")
    st.markdown('[PyGwalker : README](https://github.com/Kanaries/pygwalker)')

    

if __name__ == '__main__':
    main()
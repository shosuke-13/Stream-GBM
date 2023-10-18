import pandas as pd
import streamlit as st
import pygwalker as pyg
from main import ui_analysis
 
st.set_page_config(layout="wide", page_icon="🧊")


def default_dashboard():
    df = pd.read_csv('sample/sample_dataset.csv')
    
    # Graphic Walker
    if df is not None:
        output = pyg.walk(df, env='Streamlit')
        st.write(output)

 
def main():
    ui_analysis()
    st.markdown("## - EDA using PyGwalker -")
    st.info("Visualization your dataset using PyGwalker", icon="ℹ️")
    st.markdown("---")
    
    st.write(':sunglasses: Default dataset is sample. Please upload your dataset')
    if st.button("Create Dummy Dataset"):
        df = None
        input = st.file_uploader("Choose a CSV file")
        if input is not None:
            df = pd.read_csv(input)
                

        # Graphic Walker
        if df is not None:
            output = pyg.walk(df, env='Streamlit')
            st.write(output)
            
    else : default_dashboard()
    
    st.markdown("---")
    st.markdown('[PyGwalker : README](https://github.com/Kanaries/pygwalker)')

    

if __name__ == '__main__':
    main()
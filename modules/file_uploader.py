import streamlit as st
import pandas as pd


# upload csv file for model training
def upload():
    # analysis section 1.1    
    # first file uploader
    upload_csv = st.file_uploader('upload csv',type='csv',label_visibility="hidden")
    
    # if dataset file is uploaded, view this dataframe
    if upload_csv is not None:
        
        # Can be used wherever a "file-like" object is accepted:
        upload_csv = pd.read_csv(upload_csv)
        st.write(upload_csv.head(5))
    
    return upload_csv

# upload csv file for prediction all points data
def upload_all():
    #analysis section 1.2
    # second file uploader
    all_points = st.file_uploader('upload all points data',type='csv',label_visibility="hidden")
    
    # if dataset file is uploaded, view this dataframe
    if all_points is not None:
        
        # Can be used wherever a "file-like" object is accepted:
        all_points = pd.read_csv(all_points)
        st.write(all_points.head(5))
    
    return all_points
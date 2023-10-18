import streamlit as st
import pandas as pd


def upload():
    upload_csv = st.file_uploader('upload csv',type='csv',label_visibility="hidden")
    
    if upload_csv is not None:
        upload_csv = pd.read_csv(upload_csv)
        st.write(upload_csv.head(5))
    
    return upload_csv


def upload_all():
    """only use all points data (This function will be removed)"""
    st.markdown('### upload all points GIS-data')
    all_points = st.file_uploader('upload all points data',type='csv',label_visibility="hidden")
    
    if all_points is not None:
        all_points = pd.read_csv(all_points)
        st.write(all_points.head(5))
    
    return all_points

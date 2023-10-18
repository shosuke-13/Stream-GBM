import streamlit as st
import pandas as pd
import numpy as np
from main import ui_analysis


st.set_page_config(layout="centered", page_icon=":shark:")


def main():
    ui_analysis()
    st.markdown("## - Create Dummy Dataset -")
    st.info("Select number of rows and columns, you can download sample dataset", icon="ℹ️")
    st.markdown("---")
    
    st.markdown("#### Slide bar to select number of rows and columns")

    # User input for number of rows and columns
    num_rows = st.slider("Number of Rows", min_value=1, max_value=1000, value=100)
    num_columns = st.slider("Number of Columns", min_value=2, max_value=10, value=5)

    # Generate dummy data based on user input
    data = pd.DataFrame(np.random.randn(num_rows, num_columns), columns=[f"Feature {i+1}" for i in range(num_columns)])
    data["Target"] = data.sum(axis=1) + np.random.normal(0, 1, num_rows)

    st.write("Generated Dummy Data:")
    st.write(data)

    if st.button("Save Sample-Data to CSV"):
        csv_filename = "sample_dataset.csv"
        data.to_csv(csv_filename, index=False)
        st.success(f"Data saved to {csv_filename}")


if __name__ == '__main__':
    main()
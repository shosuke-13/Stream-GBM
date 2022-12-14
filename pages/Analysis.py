import streamlit as st
import pandas as pd
from modules import model
from Stream_GBM import ui_analysis

from modules import create_figure
#upload csv file
def upload():
    #analysis section 1
    st.markdown('---')
    st.subheader('1. Upload Model Dataset(csv)')
    
    upload_csv = st.file_uploader('',type='csv')
    if upload_csv is not None:
        # Can be used wherever a "file-like" object is accepted:
        upload_csv = pd.read_csv(upload_csv)
        st.write(upload_csv)
    
    return upload_csv


#select features,categorical,objective
def config_dataset(csv_dataset):
    #analysis section 2
    st.markdown('---')
    st.subheader('2. Config Model Dataset')

    #multi select box -> categorical_features/explanatory_variable
    categorical_features = st.multiselect('Categorical Features',\
        csv_dataset.columns.values)
    st.write(categorical_features)
    print(categorical_features)

    explanatory_variable = st.multiselect('Selected Features',\
        csv_dataset.columns.values)
    st.write(explanatory_variable)

    #single selectbox -> objective_variable
    objective_variable = st.selectbox('Selected Objective variable',\
        csv_dataset.columns.values)
    st.write(objective_variable)
    
    return categorical_features,explanatory_variable,objective_variable


#show model parameters
def model_parameter():
    #analysis section 3 (model parameter)
    st.markdown('---')
    st.subheader('3. Model Parameters')
    st.code("""params = {
                    'boosting_type':'gbdt',
                    'objective':'multiclass',
                    'metric':'multi_logloss',
                    'num_leaves':8,
                    'learning_rate':0.1,
                    'n_estimators':1000,
                    'random_state':0
                } """)
    

#start model training or not
def check_button():
    st.markdown('---')
    st.subheader('4. Model Analysis')
    st.warning('Please fill the config model dataset form')
    checked = st.button('Start analysis')
    
    return checked


#conduct model function
def model_conduct(checked,upload_csv,categorical_features,\
                                explanatory_variable,objective_variable):
    if bool(checked) == True:
        # translate csv to pandas dataframe
        #upload_csv = pd.DataFrame(upload_csv)
        
        # get explanatory_variable and objective_variable
        X, y = upload_csv.loc[:,explanatory_variable], upload_csv.loc[:,objective_variable]
        
        # conduct model function (Light GBM)
        clf,y_valid,predicted = model.model(X,y,categorical_features)
        st.success('Successed!')
        
        return clf,y_valid,predicted
    

def result(clf,y_valid,predicted):
    """
    Results
    - datavisualization
    - Accuracy
    - TP / TN / FP / FN
    - Confusion matrix
    - feature imoprtance
    """
    
    create_figure.conf_mat(y_valid,predicted)
    create_figure.met_imp(clf)
    
    

def main():
    #Base UI
    ui_analysis()
    
    #csv file uploader
    upload_csv = upload()

    #input dataset to config_dataset method()
    #Development -> df_toyota
    #Deploy -> upload_csv
    if upload_csv is not None:
        categorical_features,explanatory_variable,\
            objective_variable = config_dataset(upload_csv)
            
        #show model parameters,check model either conduct or not
        model_parameter()
        checked = check_button()
        
        if bool(checked) == True:
            #model trainnig and vaildation
            clf,y_valid,predicted = model_conduct(checked,upload_csv,categorical_features,\
                explanatory_variable,objective_variable)
            
            result(clf,y_valid,predicted)


    else:
        st.markdown('---')
        st.subheader('2. Config Model Dataset')
        st.caption('Please upload dataset csv file')
        
        st.markdown('---')
        st.subheader('3. Model Parameters')
        st.caption('Please upload dataset csv file')
        
        st.markdown('---')
        st.subheader('4. Model Analysis')
        st.caption('Please upload dataset csv file')


if __name__ == '__main__':
    main()
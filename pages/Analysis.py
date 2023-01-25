import streamlit as st
import pandas as pd
from sklearn.metrics import accuracy_score

from modules import model
from Stream_GBM import ui_analysis
from modules import create_figure,file_uploader


def upload():
    dataset = st.file_uploader('choose a csv file',label_visibility='hidden')
    
    return dataset

#select features,categorical,objective
def config_dataset(csv_dataset):
    #analysis section 2
    st.markdown('---')
    st.subheader('2. Config Model Dataset')

    #multi select box -> categorical_features/explanatory_variable
    categorical_features = st.multiselect('Categorical Features', csv_dataset.columns.values)
    st.write(categorical_features)

    explanatory_variable = st.multiselect('Selected Features', csv_dataset.columns.values)
    st.write(explanatory_variable)

    #single selectbox -> objective_variable
    objective_variable = st.selectbox('Selected Objective variable', csv_dataset.columns.values)
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
    

# start model training or not
def check_button():
    st.markdown('---')
    st.warning('Please fill the config model dataset form')
    st.subheader('4. Model Analysis')
    
    # click button -> start model training and predict
    checked = st.button('Start analysis')
    
    return checked


# conduct model function
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
    - Accuracy
    - Confusion matrix
    - Training process
    - Feature imoprtance
    """
    st.markdown(f'### Accuracy : {accuracy_score(y_valid,predicted)}')
    
    result_conf, result_metric, result_fimp = st.tabs(['Confusion Matrix', 'Metrics', 'Feature Importances'])
    with result_conf:
        create_figure.conf_mat(y_valid,predicted)
    with result_metric:
        create_figure.metric(clf)
    with result_fimp:
        create_figure.feature_importances(clf)
 
 
def analysis_predict(upload_csv,all_points):
    
    # input dataset to config_dataset method()
    if upload_csv is not None:
        categorical_features,explanatory_variable,\
            objective_variable = config_dataset(upload_csv)
            
        #show model parameters,check model either conduct or not
        model_parameter()
        checked = check_button()
        
        # keep widget
        st.session_state['train'] = bool(checked)
        
        # if check button clicked, start model training and classification
        if st.session_state['train'] == True:
            
            # model trainnig and vaildation
            clf, y_valid, predicted = model_conduct(checked,upload_csv,categorical_features,\
                explanatory_variable,objective_variable)
            
            # plot results
            result(clf,y_valid,predicted)
            
            # drop NaN cells (reduce dataset size), select explanatory variables
            allPoints_dropped = all_points.dropna()\
                                    .loc[:,explanatory_variable]
            
            # predict allpoint data and view dataframe(dataset and results)    
            predicted_allPoints = pd.DataFrame(clf.predict(allPoints_dropped))
            
            col_all, col_classified = st.tabs(['All points dataset (dropped)', 'Classified'])
            
            with col_all:
                st.write(allPoints_dropped.head(5))   
            
            with col_classified: 
                st.write(predicted_allPoints.head(5))
            
            # download classification results
            st.download_button( "Press to Download",
                                predicted_allPoints.to_csv(),
                                "dataset_statics.csv",
                                "text/csv",
                                 key='download-csv' )
            
    else:
        # before upload dataset file, show this
        st.markdown('---')
        st.subheader('2. Config Model Dataset')
        st.caption('Please upload dataset csv file')
        
        st.markdown('---')
        st.subheader('3. Model Parameters')
        st.caption('Please upload dataset csv file')
        
        st.markdown('---')
        st.subheader('4. Model Analysis')
        st.caption('Please upload dataset csv file')
            

def main():
    # Base UI
    ui_analysis()
    st.subheader('1. Upload Model Dataset (csv)')
    
    # csv file uploader
    upload, upload_all = st.tabs(['Model Training Dataset', 'All Points Dataset'])
    with upload:
        upload_csv = file_uploader.upload()
    with upload_all:
        all_points = file_uploader.upload_all()

    # analysis section
    analysis_predict(upload_csv,all_points)


if __name__ == '__main__':
    main()
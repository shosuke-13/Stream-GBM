import streamlit as st
import pandas as pd
from sklearn.metrics import accuracy_score
from modules import model
from main import ui_analysis
from modules import create_figure,file_uploader


def upload():
    dataset = st.file_uploader("choose a csv file",label_visibility="hidden")
    
    return dataset


def config_dataset(csv_dataset):
    #analysis section : select features,categorical,objective
    st.markdown("---")
    st.subheader("2. Config Model Dataset")
    st.write("Select the categorical, explanatory, and objective variables. The data chosen for the explanatory variables will be used to train the model.")
    st.warning("Please fill the config model dataset form")

    # multi select box -> categorical_features/explanatory_variable
    categorical_features = st.multiselect("Categorical Features", csv_dataset.columns.values)
    st.write(categorical_features)

    explanatory_variable = st.multiselect("Selected Features", csv_dataset.columns.values)
    st.write(explanatory_variable)

    # single selectbox -> objective_variable
    objective_variable = st.selectbox("Selected Objective variable", csv_dataset.columns.values)
    st.write(objective_variable)
    
    return categorical_features,explanatory_variable,objective_variable
    

def check_button():
    # start model training or not
    st.markdown("---")
    st.subheader("4. Model Analysis")
    st.write("Press the button to start learning the model. Check the following points")
    st.markdown("- Have you uploaded two sets of data, one for model training and the other for predicting?")
    st.markdown("- Have you filled out the model setup form?")
    st.write("If you have done both of the above, click the button.")
    
    # click button -> start model training and predict
    checked = st.button("Start Model Training")
    
    return checked


def model_conduct(checked,upload_csv,categorical_features,\
                                explanatory_variable,objective_variable):
    if bool(checked) == True:       
        # get explanatory_variable and objective_variable
        X, y = upload_csv.loc[:,explanatory_variable], upload_csv.loc[:,objective_variable]
        
        # conduct model function (Light GBM)
        clf,y_valid,predicted = model.model(X,y,categorical_features)
        
        st.success(f"Successed, Classification Accuracy is {accuracy_score(y_valid,predicted)} !", icon="✅")
        
        return clf,y_valid,predicted
    

def result(clf,y_valid,predicted):
    #analysis section 4 (model analysis)
    result_conf, result_metric, result_fimp = st.tabs(["Confusion Matrix", "Metrics", "Feature Importances"])
   
    with result_conf:
        create_figure.conf_mat(y_valid,predicted)
        
    with result_metric:
        create_figure.metric(clf)
        
    with result_fimp:
        create_figure.feature_importances(clf)
 
 
def analysis_predict(upload_csv,to_predict):
    # input dataset to config_dataset method()
    if (upload_csv is not None and to_predict is not None):
        categorical_features,explanatory_variable,\
            objective_variable = config_dataset(upload_csv)
            
        # show model parameters,check model either conduct or not
        # model_parameter()
        checked = check_button()
        
        # keep widget
        st.session_state["train"] = bool(checked)
        
        # if check button clicked, start model training and classification
        if st.session_state["train"] == True:
            
            # model trainnig and vaildation
            clf, y_valid, predicted = model_conduct(checked,upload_csv,categorical_features,\
                explanatory_variable,objective_variable)
            
            # drop NaN cells (reduce dataset size), select explanatory variables
            toPredict_dropped = to_predict.dropna()\
                                    .loc[:,explanatory_variable]
            
            # predict  and view dataframe(dataset and results)    
            predicted_toPredict = pd.DataFrame(clf.predict(toPredict_dropped)).rename(columns={0:"Group Predictions"})
            
            st.markdown("#### Results to donwnload")
            col_all, col_classified = st.tabs(["toPredict dataset (dropped NaN)", "Classified"])
            
            with col_all:
                st.markdown("###### First 5 lines")
                st.write(toPredict_dropped.head(5))
                
                st.markdown("###### Descriptive statistics")
                st.write(toPredict_dropped.describe())
            
            with col_classified: 
                st.markdown("###### First 5 lines")
                st.write(predicted_toPredict.head(5))
                
                st.markdown("###### Descriptive statistics")
                st.write(predicted_toPredict.rename(columns={0:"Group Predictions"}).describe())
            
            # download classification results
            st.download_button( "Press to Download",
                                predicted_toPredict.to_csv(),
                                "dataset_statics.csv",
                                "text/csv",
                                 key="download-csv" )
            
            
            # plot results
            st.markdown("#### Model Evaluation")
            result(clf,y_valid,predicted)
            
    else: st.error("No dataset available") # before upload dataset file
            

def main():
    # Base UI
    ui_analysis()
    st.info("Model training and predict page", icon="ℹ️")
    st.markdown("---")
    
    st.subheader("1. Upload Model Dataset (csv)")
    st.write("Please upload your dataset you want to train and predict.Please browse the csv file on each of the two tabs, an error will occur if neither is uploaded.")
    st.warning("Data column names must be aligned")
    
    # csv file uploader
    upload, upload_all = st.tabs(["Model Training Dataset", "Predict Dataset"])
    
    with upload:
        st.markdown("###### please upload your dataset you want to train.")
        upload_csv = pd.DataFrame(file_uploader.upload())
        
    with upload_all:
        st.markdown("###### please upload your dataset you want to predict.")
        to_predict = pd.DataFrame(file_uploader.upload_all())

    # analysis section
    analysis_predict(upload_csv,to_predict)


if __name__ == "__main__":
    main()
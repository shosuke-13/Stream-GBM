import streamlit as st
import matplotlib.pyplot as plt
import lightgbm as lgb
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay


def conf_mat(y_valid,predicted):
    plt.figure(figsize=(8, 8))
    
    #plot confusino matrix
    cm_LR = confusion_matrix(y_valid,predicted)
    cm_display = ConfusionMatrixDisplay(cm_LR).plot(cmap=plt.cm.summer)
    
    st.pyplot(plt)
    

def metric(clf):
    # plot training process
    lgb.plot_metric(clf,figsize=(7, 7))
    
    st.pyplot(plt)
    

def feature_importances(clf):
    # plot feature importances
    lgb.plot_importance(clf,figsize=(8, 8))
    
    st.pyplot(plt)
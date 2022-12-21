import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import lightgbm as lgb
from sklearn.metrics import confusion_matrix


#plot confusino matrix
def conf_mat(y_valid,predicted):
    plt.figure(figsize=(10, 10))
    cm_LR = confusion_matrix(y_valid,predicted)
    sns.heatmap(cm_LR, square=True, cbar=True, annot=True, cmap='Greens')
    
    plt.title('Confusion-Matrix')
    plt.xlabel("Predicted", fontsize=15)
    plt.ylabel("True Label", fontsize=15)
    
    st.markdown('- #### Confusion matrix')
    st.pyplot(plt)
    
    
# plot training process
def metric(clf):
    lgb.plot_metric(clf,figsize=(10, 8))
    
    st.markdown('- #### Metric during training')
    st.pyplot(plt)
    

# plot feature importances
def feature_importances(clf):
    lgb.plot_importance(clf,figsize=(10, 8))
    
    st.markdown('- #### Feature imoprtances')
    st.pyplot(plt)
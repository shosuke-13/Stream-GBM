import seaborn as sns
import matplotlib.pyplot as plt
import lightgbm as lgb
from sklearn.metrics import confusion_matrix

def conf_mat(y_valid,predicted):
    plt.figure(figsize=(11, 11))
    cm_LR = confusion_matrix(y_valid,predicted)
    sns.heatmap(cm_LR, square=True, cbar=True, annot=True, cmap='Greens')
    
    plt.title('Confusion-Matrix')
    plt.xlabel("Predicted", fontsize=15)
    plt.ylabel("True Label", fontsize=15)
    plt.savefig('./figures/Confusion_matrix.png')
    
def met_imp(clf):
    metric = lgb.plot_metric(clf,figsize=(8, 6))
    plt.savefig('figures/metric.png')
    
    importance = lgb.plot_importance(clf,figsize=(12, 10))
    plt.savefig('./figures/importance.png')

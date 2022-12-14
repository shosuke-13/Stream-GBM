import pandas as pd
import lightgbm as lgb
from sklearn.model_selection import train_test_split
from sklearn import preprocessing

def convert_df(df):
           return df.to_csv(index=False).encode('utf-8')
       
def model(X,y,categorical_features):
    # Label encoder instance
    le = preprocessing.LabelEncoder()
    y = le.fit_transform(y)
    
    for item in categorical_features:
        if item not in X:
            categorical_features.remove(item)
        
    
    X_train,X_valid,y_train,y_valid = train_test_split(X,y,test_size=0.3,random_state=0)
    params = {
                'boosting_type':'gbdt',
                'objective':'multiclass',
                'metric':'multi_logloss',
                'num_leaves':8,
                'learning_rate':0.1,
                'n_estimators':1000,
                'random_state':0
            } 

    clf = lgb.LGBMClassifier(**params)

    clf.fit(
        X_train, 
        y_train,
        eval_set = [(X_train, y_train),(X_valid, y_valid)],
        categorical_feature = categorical_features,
        early_stopping_rounds=50)

    predicted = clf.predict(X_valid)
    
    return clf,y_valid,predicted


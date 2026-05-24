import pandas as pd
import numpy as np
import utils
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_regression

import joblib

def data_cleaning(df):
    
    f_num = df.select_dtypes(include="number").columns
    f_cat = df.select_dtypes(include="object").columns
    
    for col in f_num:
        df[col] = df[col].fillna(df[col].mean())
        
    for col in f_cat:
        df[col] = df[col].fillna(df[col].mode())
    
    df = df.drop_duplicates()
    
    return df

        
def preprocess(df,prediction_column):
    
    Encoder = LabelEncoder()
    
    ad = df.select_dtypes(include= "object").columns
    print(ad)
    for a in  ad:
        df[a] = Encoder.fit_transform(df[a])
        
    
    # X and Y splitting
    X = df.drop(prediction_column, axis=1)
    y = df[prediction_column]
    
    # Remove Outliars
    X, y = utils.clean_outliers(X,y)
    
    # Feature Selection
    X = feature_selection(X,y)
    

    # Data splitting 
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    return X_train, X_test, y_train, y_test
   

def train_model(X_train,Y_train):
    model = LinearRegression()
    model.fit(X_train,Y_train)
    
    return model


def evaluate(model,X_test,Y_test):
    
    Y_pred = model.predict(X_test)
    y_sig=[]
    for i in Y_pred:
        a=(sigmoid(i))
        if a>=0.5:
            y_sig.append(1)#versicolor
        else:
            y_sig.append(0)#verginica
    CM = confusion_matrix(y_sig,Y_test)
    print(CM)
    score = accuracy_score(y_sig,Y_test)
    print("score",score*100)
    print(y_sig)
    return CM,score

def feature_selection(X,y):
            
    selector = SelectKBest(score_func=f_regression, k=5)
    X_new = selector.fit_transform(X, y)
    
    return X_new


def sigmoid(value):
    return 1 / (1 + (np.e**-value))

def main():
    df = pd.read_csv("iris.csv")
    df1 = data_cleaning(df)
    X_train, X_test, y_train, y_test = preprocess(df1,"variety")
    model = train_model(X_train,y_train)
    CM,score = evaluate(model,X_test,y_test)
    
if __name__ == '__main__':
    main()
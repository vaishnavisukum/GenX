import pandas as pd
from sklearn.preprocessing import LabelEncoder 
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
from sklearn.linear_model import LinearRegression

import utils_S

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
    X, y = utils_S.clean_outliers(X,y)
    
    # Feature Selection
    X = feature_selection(X,y)
    
    # Data Scalling part 
    Scaler = StandardScaler()
    df = Scaler.fit_transform(df)
   
    # Data splitting 
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    return X_train, X_test, y_train, y_test
   

def train_model(X_train,Y_train):
    model = LinearRegression()
    model.fit(X_train,Y_train)
    
    return model


def evaluate(model,X_test,Y_test):
    
    Y_pred = model.predict(X_test)
    
    mse = mean_squared_error(Y_test,Y_pred)
    mae = mean_absolute_error(Y_test,Y_pred)
    r2 = r2_score(Y_test,Y_pred) 
    
    return mse,mae,r2


# NEW ADDED - 14 May 2026
"""
This function maps the feature importnace for the prediction
based on that rank the features 

If any feature is not responsible for output prediction
that get removed.
"""
def feature_selection(X,y):
            
    selector = SelectKBest(score_func=f_regression, k=5)
    X_new = selector.fit_transform(X, y)
    
    return X_new


# NEW ADDED - 14 May 2026

def train_complete_model(df,y_prediction,model_name="model"):
    
    df = data_cleaning(df)
    X_train,X_test,y_train,y_test = preprocess(df,y_prediction)
    model = train_model(X_train,y_train)
    mse,mae,r2 = evaluate(model,X_test,y_test)
    
    if model_name :
        joblib.dump(model,"model.pkl")
    
    return {
        "Model" : model,
        "Error" : {
            "MSE" : mse,
            "MAE" : mae,
            "r2"  : r2
        }
    }
    
def main():
    df = pd.read_csv("iris.csv")
    print(train_complete_model(df,"sepal.width")["Model"].predict([[5.1,1.4,.2,1]]))

if __name__ == '__main__':
    main()
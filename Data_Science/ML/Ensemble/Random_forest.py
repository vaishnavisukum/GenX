import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_regression
from sklearn.ensemble import RandomForestClassifier
import joblib 
import utils

def data_cleaning(df):
    f_num = df.select_dtypes(include="number").columns
    f_cat = df.select_dtypes(include="object").columns

    for col in f_num:
        df[col] = df[col].fillna(df[col].mean())

    for col in f_cat:
        df[col] = df[col].fillna(df(col).mode()[0])

    df = df.drop_duplicates()
    return df

def preprocessing(df,prediction_column):
    x = df.drop(df[[prediction_column]] , axis=1)
    y= df[prediction_column]
    x,y = utils.clean_outliers(x,y)

    x_train , x_test ,y_train , y_test = train_test_split(x,y,test_size=0.2, random_state=42)
    return x_train, x_test, y_train, y_test

def feature_selection(x_train,y_train):
    selector = SelectKBest(score_func=f_regression, k=5)
    X_new = selector.fit_transform(x_train, y_train)
    return X_new

def train(x_train , y_train):
    model = RandomForestClassifier( n_estimators = 100 , max_depth= 12)
    model.fit(x_train , y_train)
    return model 

def evalutaion(x_test , y_test , model):
    Y_pred = model.predict(x_test)
    conf_matrix = confusion_matrix(y_test,Y_pred)
    acc_score = accuracy_score(y_test,Y_pred)
    return conf_matrix ,acc_score

def main():
    df = pd.read_csv("WineQT.csv")
    df1 = data_cleaning(df)
    x_train, x_test, y_train, y_test = preprocessing(df,"quality")
    x_new= feature_selection(x_train,y_train)
    model=train(x_train,y_train)
    conf_matrix , acc_score = evalutaion(x_test, y_test, model)
    print(f"error is {conf_matrix} and  accuracy {acc_score*100} %")

if __name__ == "__main__":
    main()
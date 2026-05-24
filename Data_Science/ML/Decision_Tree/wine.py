import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import tree
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_regression
import joblib
import utils

def data_cleaning(df):
    
    f_num = df.select_dtypes(include="number").columns
    f_cat = df.select_dtypes(include="object").columns
    
    for col in f_num:
        df[col] = df[col].fillna(df[col].mean())
        
    for col in f_cat:
        df[col] = df[col].fillna(df[col].mode()[0])

    df = df.drop_duplicates()
    
def preprocessing(df,prediction_column):
    
  # X and Y splitting
    
    x= df.drop(df[[prediction_column]],axis=1)
    y = df[prediction_column]
    x, y = utils.clean_outliers(x,y)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    return x_train, x_test, y_train, y_test
 
def train(x_train,y_train):
    
  model=tree.DecisionTreeClassifier(max_depth=9)
  model.fit(x_train,y_train)
  return model

def evaluation(x_test,y_test,model):
    Y_pred = model.predict(x_test)
    error = confusion_matrix(y_test,Y_pred)
    acc_score=accuracy_score(y_test,Y_pred)
    return error,acc_score


def main():
    df =  pd.read_csv("WineQT.csv")
    s = data_cleaning(df)
    x_train, x_test, y_train, y_test = preprocessing(df,"quality")
    model=train(x_train,y_train)
    error, acc_score = evaluation(x_test, y_test, model)
    print(f"error is {error} and  accuracy {acc_score*100} %")
    plt.figure(figsize=(12,8))
    tree.plot_tree(model)
    plt.show()
    joblib.dump(model,"model.pkl")



if __name__ == "__main__":
    main()
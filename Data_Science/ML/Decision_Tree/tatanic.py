import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.linear_model import LinearRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_regression
import joblib 

def data_cleaning(df):
    
    f_num = df.select_dtypes(include="number").columns
    f_cat = df.select_dtypes(include="object").columns
    
    for col in f_num:
        df[col] = df[col].fillna(df[col].mean())
        
    for col in f_cat:
        df[col] = df[col].fillna(df[col].mode()[0])

    df = df.drop_duplicates()
    
    return df

def preprocessing(df,prediction_column):
    
  # X and Y splitting
    x= df.drop(df[["PassengerId","Name"]],axis=1)
    new_df = pd.get_dummies(df,dtype=int)#encoding converts srtring to int

    x= new_df.drop(new_df[[prediction_column]],axis=1)
    y = new_df[prediction_column]
    
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    return x_train, x_test, y_train, y_test,new_df
   
def train(x_train,y_train):
    
  model=tree.DecisionTreeClassifier(max_depth=3)
  model.fit(x_train,y_train)
  return model

def evaluation(x_test,y_test,model):
    Y_pred = model.predict(x_test)
    error = confusion_matrix(y_test,Y_pred)
    acc_score=accuracy_score(y_test,Y_pred)
    return error,acc_score

def feature_selection(x_train,y_train):
    selector = SelectKBest(score_func=f_regression, k=5)
    X_new = selector.fit_transform(x_train, y_train)
    return X_new

def main():
    df =  pd.read_csv("Titanic-dataset.csv")
    s = data_cleaning(df)
    x_train, x_test, y_train, y_test,new_df = preprocessing(s,"Survived")
    model=train(x_train,y_train)
    error, acc_score = evaluation(x_test, y_test, model)
    print(f"error is {error} and  accuracy {acc_score*100} %")
    x_new= feature_selection(x_train,y_train)

    plt.figure(figsize=(12,8))
    tree.plot_tree(model)
    plt.show()
    joblib.dump(model,"model.pkl")
if __name__ == "__main__":
    main()
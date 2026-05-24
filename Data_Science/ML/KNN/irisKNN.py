import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import joblib

def main():
    df=pd.read_csv("./iris.csv")
    print(df.head())
    print(df.info())
    print(df.describe())

    x=df[["sepal.length","sepal.width","petal.length","petal.width"]]
    y=df["variety"]
    
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)
    model=KNeighborsClassifier(n_neighbors=9)
    model.fit(x_train,y_train)

    prediction=model.predict(x_test)
    for i,j  in zip(prediction,y_test):
        print("Pridiction is ",i)
        print("Actual  ans ",j)
    
    error=confusion_matrix(y_test,prediction)
    print(error)

    acc_score=accuracy_score(y_test,prediction)
    print(f"{acc_score*100}%")

    joblib.dump(model,"iris.pkl") #.pkl=.pickle

    sepl_leng=int(input())

if __name__ == "__main__":
    main()
import utils
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
import joblib

def data_cleaning(df):
    f_num=df.select_dtypes(include="number").columns # saves columns names of column conatining num values
    f_cat=df.select_dtypes(include="object").columns # character vlaues

    for col in f_num:
        df[col] = df[col].fillna(df[col].mean())   # fill Nan values with mean

    for col in f_cat:
        df[col] = df[col].fillna(df[col].mode())    # fill Nan values with mode
    
    df=df.drop_duplicates()

    return df

def preprocessing(df,a):
    encoder=LabelEncoder()
    f_cat = df.select_dtypes(include="object").columns

    for a in f_cat:
        df[a]=encoder.fit_transform(df[a])

    detected_outliar,clean_df=utils.z_score(df)

    y=df[a]
    x=df.drop([a],axis=1)

    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

    return x_train,x_test,y_train,y_test

def tarin_model(x_train,y_train):
    model=LinearRegression()
    model.fit(x_train,y_train)
    return model 

def evaluation(x_test,y_test,model):

    predicted=model.predict(x_test)
    MAE=mean_absolute_error(y_test,predicted)
    MSE=mean_squared_error(y_test,predicted)
    return MAE,MSE

def store_model(model):
    joblib.dump(model,"model.pkl")

def main():
    
    df=pd.read_csv("iris.csv")
    df1 = data_cleaning(df)
    x_train,x_test,y_train,y_test=preprocessing(df1,"petal.width")
    model1=tarin_model(x_train,y_train)
    MAE,MSE=evaluation(x_test,y_test,model1)
    print(f"Mean sq error {MSE}  and Mean absolute error {MAE} ")
    store_model(model1)

if __name__ == "__main__":
    main()
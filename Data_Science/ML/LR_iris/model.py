#cleaning

#preprocessing

import pandas as pd
def main():
    
    df=pd.read_csv("iris.csv")
    # removed  dupllicate values
    df = df.drop_duplicates()

    # remove space before and after data  
    df["variety"] = df["variety"].str.strip().str.lower()

    #type cast entires with numeric values
    df[["sepal.length","sepal.width","petal.length"]] = df[["sepal.length","sepal.width","petal.length"]].astype(int)

    # fill mean value in NAN values 
    df[["sepal.length","sepal.width","petal.length"]]= df[["sepal.length","sepal.width","petal.length"]].fillna(df[["sepal.length","sepal.width","petal.length"]].mean())

    df["variety"]= df["variety"].fillna(df["variety"].mode())
    #axis=0  finds in column ,dropna=True ignores missing values
    df.mode(axis=0, dropna=True) 

    #encoding
    df["variety"]=df["variety"].map({
        "Setosa":0,
        "Versicolor":1,
        "Virginica":2
    })
    print(df.info())
    
if __name__ == "__main__":
    main()
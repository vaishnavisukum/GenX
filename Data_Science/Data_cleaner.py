# 1. Split into X,Y
#2.Duplicate values
#3.fill empty value
#4.Data encoding 
#5.feature scaling0

import pandas as pd

def xy_spliter(dataset,target_variable):
    X = dataset.drop(columns = target_variable)
    y = dataset[target_variable]
    return X,y

def remove_duplicate():
    pass

def empty_values(X_columns):
    count = X_columns.isnull().count()
    print(count)

def main():
    df=pd.read_csv("Salary_preediction2.csv") 
    X,y = xy_spliter(df,"Monthly_Salary")

    df.isnull

    empty_values(X)
    print(X)
    print(y)
if __name__ == "__main__":
    main()
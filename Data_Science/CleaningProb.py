import pandas as pd

def main():
    df=pd.read_csv("data_cleaning.csv")    
    df = df.replace(r'^\s*$', None, regex=True) #converts  missing values (None), then dropna() removes them
    df.dropna(how="all", inplace=True)
    print("After removing blank spaces")
    print(df)
    print("After removing duplicates")
    df["name"] = df["name"].str.strip().str.lower()  #columns messy like " Name ", "AGE "
    df["city"] = df["city"].str.strip().str.lower()

    df = df.drop_duplicates()
    #print(df)
    df["salary"] = df["salary"].astype(int)
    df=df["salary"].fillna(df["salary"].mean())
    #print(df)
    
    print(df.info())


if __name__ == "__main__":
    main()
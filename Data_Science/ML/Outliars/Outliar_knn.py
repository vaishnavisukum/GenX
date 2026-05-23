import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
def main():
    df=pd.read_csv
    x=df[["Height_cm","Weight_kg"]]
    y=df["Label"]

    model=KNeighborsClassifier(n_neighbors=15)
    model.fit(x,y) 

    pridection=model.predict([[30,45]])
    print(pridection)


if __name__ == "__main__":
    main()
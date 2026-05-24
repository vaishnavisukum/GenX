import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
def main():
   line="-"*64
   df=pd.read_csv("./Dog_Cat.csv") 
   print(df.head)
   print(line)
   print(df.info())
   print(line)
   print(df.describe())
   print(line)
   
   x=df[["Height_cm","Weight_kg"]]
   y=df["Label"]

   model=KNeighborsClassifier(n_neighbors=15)
   model.fit(x,y) 

   pridection=model.predict([[30,45]])
   print(pridection)

if __name__ == "__main__":
    main()
import pandas as pd

def IQR(df):
    Q1 = df.quantile(0.25)
    Q2 = df.quantile(0.50)
    Q3 = df.quantile(0.75)
    Iqr = Q3 - Q1
    LB= Q1 - (1.5*Iqr)
    UB= Q3 + (1.5*Iqr)

    Outliars = [((df >= UB) & (df <= LB ))] # as we use pandas df has data type series thus & is used ,not and
    return Outliars

def main():
    df=pd.read_csv("Mango_weight.csv")
    x=df.drop(["Mango_ID","Status"],axis=1)
    y=df["Status"]
    print(IQR(x))

if __name__ == "__main__":
    main()
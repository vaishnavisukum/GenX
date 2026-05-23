import pandas as pd

def outliars(df,threshold=3):
    M=df.mean()
    S=df.std()
    z=(df-M)/S
    outliar=(z.abs()>threshold).all(axis=1) # .abs make values absolute & find values with z>3 ,all enties 
    outliar_rows=df[outliar]  
    clean_df=df[ ~ outliar]
    return outliar_rows,clean_df


def main():
    
    df=pd.read_csv("./Mango_weight.csv")
    x=df.drop(["Mango_ID","Status"],axis=1)#default is 0 =y axis,1=x axis  rows=y axis
    y=df["Status"]

    a,b=outliars(x,1.3)
    print(a) 
    print(b)
if __name__ == "__main__":
    main()
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    df = pd.read_csv("hello.csv")
    
    line = "-"*64
    print("\n\n"+line)
    print("FIRST 5 VALUES OF DATASET") 
    print(line+"\n")
    
    print(df.head())
    
    print("\n\n"+line)
    print("DIMENTIONAL INFO")
    print(line+"\n")
    df.info()
    
    print("\n\n"+line)
    print("STATISTICAL INFO OF DATASET")
    print(line+"\n")
    print(df.describe())
    
    
    print(line)
    print(line)
    
    
    state_counts = df["State Name"].value_counts()
    plt.figure(figsize=(10,10))
    plt.pie(state_counts, labels=state_counts.index,autopct="%0.1f%%")
    plt.title("Percentage of Districts per State in India")
    plt.show()
    
    state_grp = df.groupby("State Name")
    state_avg  = state_grp["Average Summer Temperature (°C)"].mean()
    
    plt.figure(figsize=(12,6))
    plt.bar(state_avg.index, state_avg.values)
    plt.xticks(rotation=90)
    plt.ylabel("Avg Summer Temperature (°C)")
    plt.title("State-wise Average Summer Temperature")
    plt.show()
    
        
    plt.figure(figsize=(12,6))
    plt.plot(state_avg.index, state_avg.values,marker="o")

    plt.xticks(rotation=90)
    plt.ylabel("Avg Temperature (°C)")
    plt.title("State-wise Average Temperature (Dotted Line Plot)")
    plt.show()
    
    df = df.dropna(subset=["State Name", "Average Summer Temperature (°C)"])
    df["State Name"] = df["State Name"].astype(str)

    plt.scatter(df["State Name"],df["Average Summer Temperature (°C)"])
    plt.xticks(rotation= 90)
    plt.show()
    
if __name__ == '__main__':
    main()

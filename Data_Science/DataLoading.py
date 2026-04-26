import pandas
def main():
    data=pandas.read_csv("height_weight1.csv")
    print(data)
    v1= data["Height"].mean()
    print(v1)
    data["Height"] = data["Height"].fillna(v1)   
    v2=data["Weight"].mean()
    print(v2)
    data["Weight"]=data["Weight"].fillna(v2)
    print(data)
    
if __name__ == "__main__":
    main()
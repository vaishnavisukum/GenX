import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

def prediction(m):
    print("Enter your Experience ")
    exp=int(input())

    print("Enter your education ")
    edu=input() 
    
    if edu.lower()=="bachelors":
        edu=0
    elif edu.lower()=="masters":
        edu=1
    elif edu.lower()=="phd":
        edu=2
    
    print(m.predict([[exp,edu]]))
    prediction(m)


def main():
    line="-"*64
    df=pd.read_csv("./salary_pred.csv")

    print(line)
    print(df.head())
    print("dimensions of dataset")
    print(df.info)
    print("stats of dataset")
    print(df.describe)
    
    df["EducationLevel"]=df["EducationLevel"].map({
        "Bachelors":0,
        "Masters":1,
        "PhD":2
    })

    print(df.head())
    # map() reassign values like here masters=1,bachelors=0 using disctionary key is unique values in that column 

    x=df[["YearsExperience","EducationLevel"]]
    y=df["Salary"]

    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
    #random_state =42 is a specific shuffeled state which can be used in again shuffeled state will be same
    model=LinearRegression()
    model.fit(x_train,y_train)

    Y_pred=model.predict(x_test)

    for i,j in zip(y_test,Y_pred):
        print(f"Actual value: {i} Predicted value {j} ")
    
    error=mean_absolute_error(y_test,Y_pred)
    print(error)

    prediction(model)
if __name__=="__main__":
    main()
#Exploratory Data Analysis

#Step 1- Load Data Set
#Step 2- Show first 5 entries of data
#Step 3- Show Dimensions of data set 
#Step 4- Show the statistics of data set  
#Step 5- Split Data into Depandent and independant data

import pandas as pd     # pd is just as a short name 

def main():
  line="-"*64
  df=pd.read_csv("./salary.csv")        # df= Data Frame
  print(line)
  print("first 5 entries")
  print(line)

  print(df.head())                #prints first 5 entries 
  print(line)
  print("Data set info")
  print(line)
 # print(df.size)                  # prints total no of entries all box included
  print(df.info())

  print(line)
  print("Data set statistics ")
  print(line)
  print(df.describe())              #shows statistical data min,max,count

  features=[
            df["Experience"],
            df["Education_Level"],
            df["Age"]]
  
  answer=[df["Salary"]]
  
  print(line)
  print("Independent Data ")
  print(line)
  print(features)
 

  print(line)
  print("Depandant Data ")
  print(line)
  print(answer)
 

if __name__ == "__main__":
    main()
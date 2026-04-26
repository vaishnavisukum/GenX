#Formula 
#LIne of regression : y=mx+c
# m= sum(x- mean(x))(y- mean(y))/(x-x_bar)**2
#c= mean(y) - m*mean(x)

import pandas as pd 
import numpy as np

def main():
    line="-"*64

    df=pd.read_csv("./bike_priceplot.csv")
    print("First 5 elements are ")
    print(df.head())
    print(line)

    print("Dimensions are ")
    print(df.info())
    print(line)

    print("Stats are ")
    print(df.describe())
    print(line)
 
    #-----------------------------------------------
    #       Linear Regression (Self -Define)
    #-----------------------------------------------
    
    #Seperate feature and answers from data set 

    feature=df["Bike_Power_CC"]
    answer=df["Bike_Price_INR"]
    
    # Split data into training data and testing data

    #Training
    x_train=[]
    y_train=[]
    for data in range(0,8):
        x_train.append(feature[data])
        y_train.append(answer[data])
    
    #Testing    
    x_test=[]
    y_test=[]
    for data in range(8,10):
        x_test.append(feature[data])
        y_test.append(answer[data])
    
    print(line)
    print("These are feature of traing",x_train)
    print("These are Y of traing",y_train)
    print(line)
   
    print(line)
    print("These are feature of testing",x_test)
    print("These are Y of testing",y_test)
    print(line)

    x_=np.mean(x_train)
    print("Mean of training features is ",x_)

    y_=np.mean(y_train)
    print("Mean of training  Y is ",y_)

    print(line)
    #x - mean(x)
    x_sub_xBar=[]
    y_sub_yBar=[]
    for data in range(0,8):
        x_sub_xBar.append(x_train[data] - x_)
        y_sub_yBar.append(y_train[data] - y_)
    print(line)
    print("x-mean(x)",x_sub_xBar)
    print("y-mean(y)",y_sub_yBar)
    print(line)

    #(x- mean(x))(y- mean(y)) 
    x_sub_xbar_X_y_sub_ybar=[] 
    for data in range(0,8):
      x_sub_xbar_X_y_sub_ybar.append(x_sub_xBar[data]*y_sub_yBar[data])
    
    print(line)
    print("(x- mean(x))(y- mean(y)) ",x_sub_xbar_X_y_sub_ybar)  
    print(line)

    #(x-mean(x))^2
    x_sub_xbar_sq=[]
    for data in range(0,8):
        x_sub_xbar_sq.append(x_sub_xBar[data]**2)
    
    print(line)   
    print("(x-mean(x))^2",x_sub_xbar_sq)
    print(line)
    
    numerator=0
    denominator=0
    for data in range(0,8):
        numerator=numerator+x_sub_xbar_X_y_sub_ybar[data]
        denominator=denominator+x_sub_xbar_sq[data]
    
    print("Sum((x- mean(x))(y- mean(y))) is",numerator)
    print("Sum((x-mean(x))^2) is ",denominator)   
    
    #Calculate slope m and Y intercept c
    m=numerator/denominator
    c=y_ - (m*x_) 
    print(line)
    print("Value of slope(m) is ",m)
    print("Value of Y intercept(c) is ",c)
    print(line)
    
    #Testing
    err=0
    for data in range(0,2):
      y_hat= (m*(x_test[data])) + c  
      errr= y_test[data]-y_hat
      err+=errr

    error=err/2
    print(line)
    print("Error mean is ",error)
    print(line)
    
if __name__ == "__main__":
    main()
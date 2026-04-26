import pandas as pd
import matplotlib.pyplot as plt 
#Step 1 - Show first 5 element
#Step 2 - Show dimensions of data and its data type 
#Step 3- Show data statistics 
#Step 4- Draw Pie chart 
def main():
    df=pd.read_csv("./hello1.csv")
    line="-"*64

    print(line)
    print("first 5 entries")
    print(line)
    print(df.head())

    print(line)
    print("Dimensions")
    print(line)
    print(df.info())

    print(line) 
    print("Stats ")
    print(line)
    print(df.describe(include="all",percentiles=[0.25,0.5,0.75]))
    
    state_name=[] 
    state_count=[]
    dist_group=df.groupby("State Name")
    for i in dist_group:
        state_count.append(len(i[1]))
        state_name.append(i[0])

    state_count_percentage=[]
    for num in state_count:
        k=(num/779)*100
        state_count_percentage.append(k)
    
   
    plt.figure(figsize=(10,10))  
    plt.pie(state_count_percentage,labels=state_name,autopct="%0.1f%%") 
    # here first parameter is partions ,    
      # here 0 defines  that after decimal ther should be only one no. 
      # autopct = auto percentage  
      # add extra % so that pie chart can take it has a value      
    plt.show()

    plt.figure(figsize=(15,10))
    plt.bar(state_name,state_count_percentage)
    plt.xticks(rotation=90)
    plt.show()
    
    
    
    
    df["Average Summer Temperature"] = pd.to_numeric(df["Average Summer Temperature"],errors="coerce")
     # as the in the csv the temp column is taken as str use to_numeric
     # coerce: Converts invalid values into NaN
    avg_temp = []

    for state, group in dist_group:
        avg = group["Average Summer Temperature"].mean()    #np.float64(40.28)
        avg_temp.append(avg)
    avg_temp = [float(x) for x in avg_temp]   
    
    plt.figure(figsize=(15,10))
    plt.bar(state_name,avg_temp)
    plt.xticks(rotation=90)
    plt.show()

if __name__ == "__main__":
    main()

    # draw a bar graph x axis= state name ,
    #                  y axis = average temp of that state
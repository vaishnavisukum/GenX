def main():
  number_of_elm=int(input("Enter no. of values"))
  list=[]
  for i in range(0,number_of_elm): # take input of list by asking user no of input from user
    k=int(input())
    list.append(k)
  print(list)
if __name__=="__main__":
  main()
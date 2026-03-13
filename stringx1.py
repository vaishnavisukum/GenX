def pattern(value:int):
  value=value+1
  for i in range(0,value):
    for j in range(0,i):
     print("*",end="") # defalut end="/n"
    print() 
def main():
  a=int(input("enter value"))
  pattern(a)

if __name__=="__main__":
  main()
def manyeven():
  odd=0
  even=0
  b=[]
  for i in b:
    b[i]=int(input("enter value"))
    b.append(b[i])
    
  for i in b:
    if(i%2!=0):
      odd=odd+1
    else:
      even=even+1
  print(f"odd no. are {odd} and even are {even} ")

def main():
  manyeven()
if __name__=="__main__":
  main()
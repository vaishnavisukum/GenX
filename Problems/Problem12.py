def manyeven(b):
  odd=0
  even=0
  for i in b:
    if(i%2!=0):
      odd=odd+1
    else:
      even=even+1
  print(f"odd no. are {odd} and even are {even} ")

def main():
  a=[1,21,3,11,5]
  manyeven(a)
if __name__=="__main__":
  main()
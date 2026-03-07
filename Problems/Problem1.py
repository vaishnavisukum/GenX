def iseven(a):
  
  for i in a:
    if(i%2 != 0):
      print("all are not even")
      return 
  print("all are even")
  return 
      
def main():
  a=[22,44,66]
  iseven(a)
  
if __name__=="__main__":
  main()
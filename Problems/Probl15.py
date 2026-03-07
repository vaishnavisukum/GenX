def main():
  i=0
  while i<=10:
    i=i+1
  list=[]
  init=True
  
  print("For stopping enter stop")
  while init:
   k=(input())
   if k!="stop":
    list.append(int(k))
   else:
     init=False
  print(list)
if __name__=="__main__":
  main()
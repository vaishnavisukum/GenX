def countalpha():
  a=input("enter string")
  list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  for i in range(1,27):
    if a==list[i]:
       yield list.index(i)

def main():
    for itm in countalpha():
     print(itm)
if __name__=="__main__":
  main()
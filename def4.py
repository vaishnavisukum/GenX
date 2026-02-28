def addition(a,b,*args):# can use anything instead of args variable
  print(a,b,args)
  c=a+b
  temp=0
  for i in args:
    temp=temp+i
  return temp+c

def main():
  vv=addition(1,2,3,4,5)
  print(vv)
if __name__=="__main__":
  main()
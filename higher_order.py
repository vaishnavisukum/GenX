def cal(a):
  return a(11,10)

def add(n,m):
  return n+m

def main():
  ret=cal(add) # gives functions reference 
  print(ret)
if __name__=="__main__":
  main()
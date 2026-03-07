def iseven(a):
  for i in a:
    if(i&1):
      print(i&1)
      return
  print(i&2)
  return

def main():
  a=[10,2,4]
  iseven(a)
if __name__=="__main__":
  main()
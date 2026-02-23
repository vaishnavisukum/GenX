a=10
def update():
  global a
  a=a+1
  return a
  
def main():
  no=update()
  print(no)
  
if __name__=="__main__":
  main()
num=0
def counter():
  global num
  num=num+1
  print(num)
  return counter()  #find a way to make the stack 2000 times as it is 1000 right now 

def main():
  counter()
if __name__=="__main__":
  main()
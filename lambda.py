def sq(num):
  return num*num
sqq=lambda num: num**2 # also a function but limitation only one statement return

def main():
  print(sq(4))
  print(sqq(7))
if __name__=="__main__":
  main()
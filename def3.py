def hello(name="jon doe"): #decleration of default argument
  print("hello ",name)


def main():
  hello("vaishnavi")
  hello()  #uses default argument
if __name__=="__main__":
  main()
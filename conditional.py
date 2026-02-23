import os

def main():
  name=input("Enter your name")
  gender=input("Enter your gender")

  if(gender=="male"):
    print("You are male")
    print("Hello",name,"how are you")
    os.system("Say hello")
  elif(gender=="female"):
    print("You are Female")
    print("Hello",name,"how are you")
  else:
    print("Pls enter valid input either male or female")
if __name__=="__main__":
  main()
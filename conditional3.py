def main():
  alf=input("Enter any alphabet : ")
  alf=alf.lower() # this is a method 
  vowel="aeiou"
  consonent="bcdfghjklmnpqrstvwxyz"
  if(alf in vowel):
    print("This is a vowel")
  elif(alf in consonent ):
    print("This is a consonent")
  else:
    print("pls enter valid input")

if __name__=="__main__":
  main()
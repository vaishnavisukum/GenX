def reverse_string(string:str):
  print("enter your string ")
  string =input()
  string=string.split(" ")
  rev_str=""
  for i in string:
    rev_str += i[-1: :-1]+" "

  return rev_str

def main():
   print("enter your string ")
   string =input()
   print(string)
if __name__=="__main__":
  main()
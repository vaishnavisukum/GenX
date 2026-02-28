def main():

  print("Enter a number")
  num=int(input())

  for i in range(1,11):
    print(f"{num} X {i}=",num*i)

if __name__ =="__main__":
  main()
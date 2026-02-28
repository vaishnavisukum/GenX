def add(a,b):
  return a+b

def calculator(a,b):
  addition=a+b
  sub=a-b
  div=a/b
  prod=a*b
  return addition,sub,div,prod 

def origin():
  return __name__

orgg=origin()
print(orgg)
# def main():
#   var=add(11,10)
#   print("addition is ",var)

#   a,b,c,d=calculator(21,22)
#   print("calculator result is ",a) 
#   print("calculator result is ",b)
#   print("calculator result is ",c)
#   print("calculator result is ",d)

# if __name__=="__main__":
#   main()
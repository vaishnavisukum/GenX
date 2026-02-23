def addd(no1,no2):
  return no1+no2

def subb(no1,no2):
  return no1-no2

def divv(no1,no2):
  return no1/no2

def prodd(no1,no2):
  return no1*no2

def modd(no1,no2):
  return no1%no2

def main():
  a=20
  b=11
  add=addd(a,b)
  sub=subb(a,b)
  div=divv(a,b)
  prod=prodd(a,b)
  mod=modd(a,b)
  print(add)
  print(sub)
  print(div)
  print(prod)
  print(mod)
if __name__=="__main__":
 main()
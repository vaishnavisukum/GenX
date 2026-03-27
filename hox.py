def val_decision(odd_func,num):
  fact=1
  n=num
  while n>0:
    fact*=n
    n-=1
  return odd_func(fact)
def oddnum(end):
  for num in range(0,end):
    if num & 1==1 :
      yield num
def main():
  for itm in val_decision(oddnum,5):
    print(itm)
if __name__=="__main__":
  main()
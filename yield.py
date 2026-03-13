def table():
   for i in range(1,11):
      yield i*2            # returns in object for that we have to use for loop to be visible 
                            # returns multiple values without being in tuple or list 
                            # the value is  not already creted it creates after each loop
                            #  

def main():     
  for itm in table():
     print(itm)

if __name__=="__main__":
  main()
import threading
addition=0
#Process /Thread 1
def add(a,b):
    global addition
    addition=a+b
    

#Process/Thread 2
def pow():
    num=addition
    print(num**2)

def main():
   t1=threading.Thread(target=add,args=(11,10))
   t2=threading.Thread(target=pow)
   t1.start()
   t2.start()
if __name__ == "__main__":
    main()
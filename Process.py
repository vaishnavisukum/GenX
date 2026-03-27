import multiprocessing 

#Process /Thread 1
def add(a,b,q):
    result=a+b
    q.put(result)

#Process/Thread 2
def pow(a):
    num=a.get()
    print(num**2)

def main():
    q=multiprocessing.Queue()
    p1=multiprocessing.Process(target=add,args=(10,11,q))
    p2=multiprocessing.Process(target=pow,args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
if __name__ == "__main__":
    main()
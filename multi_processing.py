from multiprocessing import Process
def process1():
  #  print("Hello world") 
  #  for i in range(0,1000001):
  #      if i==1000000:
  #          print("Done")
   for i in range(1,101):
      print(f"2^{i} is {2**i} ") 

def process2():
  val=1
  for i in range(1,26):
    val=i*val
    print(val)

def main():
  print("Executing P1 and P2")
  p1=Process(target=process1)
  p2=Process(target=process2)
  p1.start()
  p2.start()


if __name__ == "__main__":
    main()
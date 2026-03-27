from multiprocessing import Process
import datetime
def process1():
  
   for i in range(1,10000001):
       pass

def process2():
  val=1
  for i in range(1,1001):
    val=i*val
    

def main():
  start_time=datetime.datetime.now()
  print("Executing P1 and P2")
  
  p1=Process(target=process1)
  p2=Process(target=process2)
  p1.start()
  p2.start()
  end_time=datetime.datetime.now()
  total_time=end_time-start_time
  print(total_time)


if __name__ == "__main__":
    main()
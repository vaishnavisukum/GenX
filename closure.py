def parent(name):
  
    def hello():
      return "hello"+ name 

    def gm():
      return "Good morning"+ name
  
    def gn():
      return "good night"+ name
  
    return gm,gn,hello

def main():
  a,b,c=parent("yash")
  print(a())
  print(b())
  print(c())
if __name__=="__main__":
  main()
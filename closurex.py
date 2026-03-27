def a(num1):
  def b(num2):
    return num1+num2
  return b
def main():
  child= a(1)
  ret=child(11)
  print(ret)
if __name__=="__main__":
  main()  
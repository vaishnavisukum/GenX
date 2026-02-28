def main():
  a = [1,2,3,4,5]
  print(a)

  a.append(6) #updates the list using append() adds the element at the end
  a.append(7) 
  a.append(8)
  a.append(9)
  a.append(10)
  print(a)

  a.append(11)
  print(a)

  a.pop() #removes last element
  print(a)

if __name__=="__main__":
  main()
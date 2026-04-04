student={                  #Dictionary
    "Name":"Vaishnavi",
    "age":19,
    "surname":"Sukum"
}

number={1,2,3,4,5,6,7,8,9,10} #set
def main():
   for elements in student:
       print(student[elements])

   for set in number:
    print(set)
   print(number[0])  #no  indexing allowed
if __name__ == "__main__":
    main()
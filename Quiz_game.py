def main():
  que_set1={
     "who is national animal":["kutra","Manjar","Popat","Tiger",3],
     "which is national anthum":["Sukh karta","hanuman chalisa","jana gana mana","nacho nacho",2],
     "national flower ?":["rose","lotus","lilly","hisbiscus",1],
     "native language of maharashtra ? ":["hindi","marathi","sanskrit","urdu",1],
     "fingers in one hand":["1","4","5","8",2]
  }

  que_set2={
     "capital of india":["Mumbai","Delhi","Kolkata","Chennai",1],
    "largest planet in solar system":["Earth","Mars","Jupiter","Venus",2],
    "national bird of india":["Sparrow","Peacock","Crow","Parrot",1],
    "2 + 2 = ?":["3","4","5","6",1],
    "color of sky":["Green","Blue","Red","Yellow",1]
  }
  que_set3={
     "fastest land animal":["Lion","Tiger","Cheetah","Leopard",2],
    "who discovered gravity":["Newton","Einstein","Tesla","Edison",0],
    "national fruit of india":["Apple","Banana","Mango","Orange",2],
    "how many continents are there":["5","6","7","8",2],
    "square root of 16":["2","4","6","8",1]
  }

  que_set4={
     "largest ocean":["Atlantic","Indian","Pacific","Arctic",2],
    "currency of japan":["Yuan","Won","Yen","Dollar",2],
    "primary language of maharashtra":["Hindi","Marathi","Gujarati","Punjabi",1],
    "how many days in a week":["5","6","7","8",2],
    "opposite of hot":["Cold","Warm","Cool","Dry",0]
}
  

  question_sets=[que_set1,que_set2,que_set3,que_set4]
  terminator=True

  print("Message : for more detail type help")
  option=0
  while(terminator):
     cmd=input(">>>")
     if cmd=="exit":
        exit()
     elif cmd=="help":
        print(""" 
                To start the game say "start"
                if yo want to exit say "exit"
                if you want to choose different topic say "options"
                to add your own quiz for quiz just say "add-quiz"
              """)
        
     elif cmd=="options":
        print(""" 
                type 1 for :  MYTHOLOGY
                type 2 for :  GK
                type 3 for :  HISTORY
                type 4 for :  COMPUTER
              """)
        option=int(input(">>>"))-1 
     elif cmd=="start":
        point=0
        for questions in question_sets[option]:
          print("\n"+questions+"\n")

          for ops in range(0,len(question_sets[option][questions])-1): # OR range(0,4)
            print("\t",ops+1,question_sets[option][questions][ops]) 

         # ans=int(input())-1
          ans=input()  

          if ans.isdigit():
             ans= int(ans)-1
          elif ans=="exit":
             print(f"You scored {point}/5") 
             exit()

          if question_sets[option][questions][-1]==ans:
               point+=1
        print(f"You scored {point}/5") 

     elif cmd=="add-quiz":
        quiz={}
        options=[]   
        print("enter your Quiz Title")
        title=input()

        for question in range(1,6):
           options=[]
           print(f"Enter questions no {question}")
           key=input()

           for val in range(1,6):
              if val==5 :
                 value=int(input("Enter answer of this question "))-1 
                 allowed_ops=[1,2,3,4]
                 if value+1 in allowed_ops:
                  options.append(value)
               
              else:
                 value=input(f"Enter option {val} :")
                 options.append(value)

           quiz[key]=options

        print(quiz)
        question_sets.append(quiz)
        option=-1
        print(question_sets)
if __name__ == "__main__":
    main()